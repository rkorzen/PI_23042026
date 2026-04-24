import json
from http.server import BaseHTTPRequestHandler, HTTPServer


HOST = "127.0.0.1"
PORT = 9002
AUTH_TOKEN = "sekretny-token"


class ReusableHTTPServer(HTTPServer):
    allow_reuse_address = True


class JsonHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, payload: dict, extra_headers: dict | None = None) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        if extra_headers:
            for header, value in extra_headers.items():
                self.send_header(header, value)
        self.end_headers()
        self.wfile.write(body)

    def _require_authentication(self) -> bool:
        auth_header = self.headers.get("Authorization", "")
        expected_header = f"Bearer {AUTH_TOKEN}"
        if auth_header == expected_header:
            return True

        self._send_json(
            401,
            {
                "ok": False,
                "error": "Unauthorized",
                "hint": f"Uzyj naglowka Authorization: {expected_header}",
            },
            extra_headers={"WWW-Authenticate": "Bearer"},
        )
        return False

    def do_GET(self) -> None:
        if self.path != "/api/hello":
            self._send_json(404, {"ok": False, "error": "Not Found", "path": self.path})
            return

        if not self._require_authentication():
            return

        payload = {
            "ok": True,
            "path": self.path,
            "message": "Hello from localhost",
            "name": "Python",
            "authenticated": True,
        }
        self._send_json(200, payload)

    def do_POST(self) -> None:
        if self.path != "/api/echo":
            self._send_json(404, {"ok": False, "error": "Not Found", "path": self.path})
            return

        if not self._require_authentication():
            return

        if not self.headers.get("Content-Type", "").startswith("application/json"):
            self._send_json(415, {"ok": False, "error": "Expected application/json"})
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length)

        try:
            data = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json(400, {"ok": False, "error": "Invalid JSON payload"})
            return

        if not isinstance(data, dict):
            self._send_json(400, {"ok": False, "error": "JSON payload must be an object"})
            return

        name = str(data.get("name", "anonim"))
        message = str(data.get("message", ""))
        payload = {
            "ok": True,
            "path": self.path,
            "received": data,
            "summary": f"Odebrano wiadomosc od {name}",
            "message_length": len(message),
        }
        self._send_json(201, payload)

    def log_message(self, format: str, *args: object) -> None:
        # Keep the example quiet and focused on the HTTP exchange.
        return


def main() -> None:
    server = ReusableHTTPServer((HOST, PORT), JsonHandler)
    print(f"Serwer HTTP slucha na http://{HOST}:{PORT}")
    print("GET  /api/hello")
    print("POST /api/echo")
    print(f"Authorization: Bearer {AUTH_TOKEN}")
    print("Uruchom klienta w drugim terminalu.")
    try:
        server.handle_request()
        server.handle_request()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

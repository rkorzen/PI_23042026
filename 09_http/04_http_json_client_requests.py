#!/usr/bin/env python3
"""Klient HTTP pobierajacy i wysylajacy lokalny JSON przez requests."""

import sys

try:
    import requests
except ImportError as error:
    raise SystemExit(
        "Ten przyklad wymaga biblioteki 'requests'. Zainstaluj ja poleceniem: pip install requests"
    ) from error


HOST = "127.0.0.1"
PORT = 9002
AUTH_TOKEN = "sekretny-token"


def send_json_request(method: str, path: str, payload: dict | None = None) -> tuple[str, int, str, dict]:
    url = f"http://{HOST}:{PORT}{path}"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}

    # requests sam serializuje slownik do JSON-a, jesli uzyjemy parametru json=...
    response = requests.request(method, url, headers=headers, json=payload, timeout=5)
    response.raise_for_status()

    status_code = response.status_code
    content_type = response.headers.get("Content-Type", "")
    data = response.json()
    return url, status_code, content_type, data


def main() -> None:
    hello_url, hello_status, hello_content_type, hello_data = send_json_request("GET", "/api/hello")

    print("GET /api/hello")
    print(f"url: {hello_url}")
    print(f"status_code: {hello_status}")
    print(f"content_type: {hello_content_type}")
    print(f"name: {hello_data['name']}")
    print(f"message: {hello_data['message']}")

    payload = {
        "name": "Python",
        "message": "POST z JSON payloadem",
    }
    echo_url, echo_status, echo_content_type, echo_data = send_json_request("POST", "/api/echo", payload)

    print()
    print("POST /api/echo")
    print(f"url: {echo_url}")
    print(f"status_code: {echo_status}")
    print(f"content_type: {echo_content_type}")
    print(f"summary: {echo_data['summary']}")
    print(f"message_length: {echo_data['message_length']}")
    print(f"received_name: {echo_data['received']['name']}")


if __name__ == "__main__":
    sys.exit(main())

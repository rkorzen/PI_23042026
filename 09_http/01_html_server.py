from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 9003
HTML_PAGE = """
<html>
    <head>
        <title>Hello world</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <ul>
            <li><a href="/docs">Documentation</a></li>
            <li><a href="/tutorial">Tutorial</a></li>
            <li><a href="/faq">FAQ</a></li>
        </ul>
    </body>
</html>
"""


class HtmlHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = HTML_PAGE.encode("UTF-8")
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

def main():
    server = HTTPServer((HOST, PORT), HtmlHandler)
    print(f"Serving HTTP on http://{HOST}:{PORT}")

    try:
        server.handle_request()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
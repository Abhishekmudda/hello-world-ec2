# hello.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World from EC2!")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8080)  # Listen on all interfaces on port 8080
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on port 8080...")
    httpd.serve_forever()

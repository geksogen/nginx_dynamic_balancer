import socket
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Отвечаем на любые GET-запросы
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Получаем имя контейнера (hostname)
        hostname = socket.gethostname()
        response = f"Hello from backend! My container ID is: {hostname}\n"

        self.wfile.write(response.encode('utf-8'))


if __name__ == '__main__':
    print("Backend server starting on port 8080...")
    server = HTTPServer(('0.0.0.0', 8080), RequestHandler)
    server.serve_forever()
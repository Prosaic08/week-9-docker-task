from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the length of the data
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the POST body
        body = self.rfile.read(content_length).decode('utf-8')
        print(body)

        # Respond with something
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"POST received")
    def log_message(self, format, *args):
        return

# Run the server
if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8080
    server = HTTPServer((host, port), SimpleHandler)
    server.serve_forever()

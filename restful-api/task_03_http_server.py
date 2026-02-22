#!/usr/bin/python3

import json
import http.server
from http.server import HTTPServer


class Simpleapi(http.server.BaseHTTPRequestHandler):
    """
    Cette class est un gestionnaire de requete. Elle
    hérite de http.server...
    """
    def do_GET(self):
        """
        Cette fonction va envoyer les réponses selon
        les différents chemins qui prends.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            datainfo = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(datainfo).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), Simpleapi)
    print(f"Server running on port {PORT}")
    server.serve_forever()

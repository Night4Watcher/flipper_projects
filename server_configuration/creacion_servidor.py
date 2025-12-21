from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "192.168.1.50"  # cámbialo por la IP que quieras
PORT = 8080            # puerto

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Sirviendo en http://{HOST}:{PORT}")
    server.serve_forever()


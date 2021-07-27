from http.server import HTTPServer, BaseHTTPRequestHandler


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        foo = bytes('bar', 'utf')
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(foo)

        if self.send_response == 200:
            self.wfile.write(foo)
        else:
            self.send_response(404)


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':    
    main()
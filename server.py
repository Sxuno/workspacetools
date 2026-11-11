# Test server

import pathlib

ROOT = pathlib.Path(__file__).parent.parent.resolve()
SCRIPTS = ROOT
CONTENT = ROOT

print(ROOT)

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print('--- request ---')
        print('method : GET')
        endpoint = pathlib.Path(self.path).parent
        print(f'endpoint : {pathlib.Path(self.path).parent}')
        request = self.path.split('/')[-1]
        print(f'request : {request}')
    
        request = self.path.lstrip('/')
        print('***')
        print(request)
        print(ROOT)
        path = pathlib.Path(ROOT / request)
        print(path)

        if path.is_file() and path.suffix in ('.html', '.js', '.css', '.svg', '.png', '.onnx'):
            self.send_response(200)
            self.send_header('Content-Type', {
                '.html' : 'text/html',
                '.css' : 'text/css',
                '.js' : 'application/javascript',
                '.svg' : 'image/svg+xml',
                '.png' : 'image/png',
                '.onnx': 'application/octet-stream'
            }[path.suffix])
            self.end_headers()
            self.wfile.write(path.read_bytes())
            return

        self.send_error(404)

server = HTTPServer(('localhost', 8000), RequestHandler)
server.serve_forever()
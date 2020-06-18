import os
import http.server as hs

class RequestHandler(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        self.full_path = os.getcwd() + self.path
        print(self.path)
        print(self.full_path)
        pass

httpAddress = ('',8000)
httpd = hs.HTTPServer(httpAddress,RequestHandler)
httpd.serve_forever()
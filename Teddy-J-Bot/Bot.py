import ast
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

class ServiceHandler(BaseHTTPRequestHandler):
	
  def do_GET(self):
    print(self.path)


  def do_POST(self):
    content_len = int(self.headers.get('Content-Length'))
    post_body = self.rfile.read(content_len)  
    body = ast.literal_eval(post_body.decode("utf-8"))
    response={
      "test":"test"
    }
    self.send_response(HTTPStatus.OK.value)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(bytes(json.dumps(response, ensure_ascii=False), 'utf-8'))
  
		
   
#Server Initialization
server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
server.serve_forever()
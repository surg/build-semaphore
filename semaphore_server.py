import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

job_stats = None

class MyRequestHandler(SimpleHTTPRequestHandler):	
	def serve_stats(s): 
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write(s.job_stats.job_stats())

	def do_GET(self):
		if self.path.startswith('/statuses'):
			self.serve_stats()
		else:
			SimpleHTTPRequestHandler.do_GET(self)

class SemaphoreServer(object):
	def __init__(self, js, port):
		self.job_stats = js
		self.port = port

	def start(self):
		HandlerClass = MyRequestHandler
		ServerClass  = BaseHTTPServer.HTTPServer
		Protocol     = "HTTP/1.0"

		server_address = ('localhost', self.port)

		HandlerClass.protocol_version = Protocol
		HandlerClass.job_stats = self.job_stats
		httpd = ServerClass(server_address, HandlerClass)

		sa = httpd.socket.getsockname()
		print "Serving HTTP on", sa[0], "port", sa[1], "..."
		httpd.serve_forever()
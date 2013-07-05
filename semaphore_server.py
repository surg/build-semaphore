import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import json

class MyRequestHandler(SimpleHTTPRequestHandler):	
	def update(self):
		stats = self.job_stats.job_stats()
		self.serve_stats(stats)
		for l in self.listeners:
			l.update(stats)

	def serve_stats(s, stats): 
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write(json.dumps(stats))

	def do_GET(self):
		if self.path.startswith('/statuses'):
			self.update()
		else:
			SimpleHTTPRequestHandler.do_GET(self)

class SemaphoreServer(object):
	def __init__(self, js, port, listeners):
		self.job_stats = js
		self.port = port
		self.listeners = listeners
		semaphore = self

	def start(self):
		HandlerClass = MyRequestHandler
		ServerClass  = BaseHTTPServer.HTTPServer
		Protocol     = "HTTP/1.0"

		server_address = ('localhost', self.port)

		HandlerClass.protocol_version = Protocol
		HandlerClass.job_stats = self.job_stats
		HandlerClass.listeners = self.listeners
		httpd = ServerClass(server_address, HandlerClass)

		sa = httpd.socket.getsockname()
		print "Serving HTTP on", sa[0], "port", sa[1], "..."
		httpd.serve_forever()
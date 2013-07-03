#!/usr/bin/python
import sys
from urllib import urlopen
from datetime import datetime
import threading
import re
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

POLL_INTERVAL = 60

def job_stats(jenkins, jobs):
	stats = '{'
	for j in jobs:
		url = "%s/job/%s/lastBuild/buildStatus" % (jenkins, j)
		print "Reading ", url
		url = urlopen(url).geturl()
		stats += "\"%s\": \"%s\"," % (j, re.search('48x48/([^.]+)\.', url).group(1))
	stats += '}'	
	print str(datetime.now()), stats
	with open("statuses.json", "w+") as f: 
		f.write(stats)
	threading.Timer(POLL_INTERVAL, lambda: job_stats(jenkins, jobs)).start()

def read_config(config_file_name):
	config = None
	with open(config_file_name) as f:
		config = f.read()
	cfg = eval(config)
	return cfg

def start_server(config):
	HandlerClass = SimpleHTTPRequestHandler
	ServerClass  = BaseHTTPServer.HTTPServer
	Protocol     = "HTTP/1.0"

	port = int(config.get('port', 8000))
	server_address = ('localhost', port)

	HandlerClass.protocol_version = Protocol
	httpd = ServerClass(server_address, HandlerClass)

	sa = httpd.socket.getsockname()
	print "Serving HTTP on", sa[0], "port", sa[1], "..."
	httpd.serve_forever()

config_file_name = 'config.py'
if (len(sys.argv) > 1):
	config_file_name = sys.argv[1]
config = read_config(config_file_name)

# Start polling jenkins
job_stats(config['jenkins'], config['jobs'])

# Start simple http server to make html page available via http.
# This is necessary mostly to allow jquery querying file in the same domain. 
start_server(config)
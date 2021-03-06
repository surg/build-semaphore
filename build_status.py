#!/usr/bin/python
import sys
import threading
from semaphore_server import SemaphoreServer
import job_stats
from arduino import Arduino

POLL_INTERVAL = 60

def read_config(config_file_name):
	config = None
	with open(config_file_name) as f:
		config = f.read()
	cfg = eval(config)
	return cfg

config_file_name = 'config.py'
if (len(sys.argv) > 1):
	config_file_name = sys.argv[1]
config = read_config(config_file_name)

# Start polling jenkins
if not config.get('offline', False):
	js = job_stats.JobStats(config['jenkins'], config['jobs'])
else: 
	print "Running in offline mode"
	js = job_stats.OfflineJobStats()

listeners = []
if config.get('arduino', False):
	listeners.append(Arduino(config['arduino_port']))
# Start simple http server to make html page available via http.
# This is necessary mostly to allow jquery querying file in the same domain. 
SemaphoreServer(js, config.get('port', 8000), listeners).start()
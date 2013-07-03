#!/usr/bin/python
from urllib import urlopen
from datetime import datetime
import threading
import re

def job_stats():
	jobs = ['SDP_3.24.X_TEST_SMOKE_BCOM-RunTest', 'SDP_3.24.X_TEST_SMOKE_MCOM-RunTest', 
			'SDP_UN_3.24.X_SMOKE_FUNC-RunTest', 'SDP_UN_3.24.X_SMOKE_STUB-RunTest','SDP_3.24.X_BUILD', 'SDP-Functional-Promote_3.24.X-DEPLOY']
	stats = '{'
	for j in jobs:
		url = urlopen("http://mdc3vr1192.tun.c4d.griddynamics.net:40006/jenkins/job/%s/lastBuild/buildStatus" % j).geturl()
		stats += "\"%s\": \"%s\"," % (j, re.search('48x48/([^.]+)\.', url).group(1))
	stats += '}'	
	print str(datetime.now()), stats
	with open("statuses.json", "w+") as f: 
		f.write(stats)
	threading.Timer(60, job_stats).start()

# start calling f now and every 60 sec thereafter
job_stats()
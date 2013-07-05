from urllib import urlopen
import re
from datetime import datetime
import json
from collections import OrderedDict

class JobStats(object):
	def __init__(self, jenkins, jobs):
		self.jenkins = jenkins
		self.jobs = jobs

	def job_stats(self):
		stats = OrderedDict()
		for j in self.jobs:
			url = "%s/job/%s/lastBuild/buildStatus" % (self.jenkins, j)
			print "Reading ", url
			url = urlopen(url).geturl()
			stats[j] = re.search('48x48/([^.]+)\.', url).group(1)
		return stats

	def to_file():
		stats = job_stats(jenkins, jobs)
		print str(datetime.now()), stats
		with open("statuses.json", "w+") as f: 
			f.write(stats)

class OfflineJobStats(object):
	def job_stats(self):
		with open('statuses.json', 'r') as f:
			return json.loads(f.read())
from urllib import urlopen
import re
from datetime import datetime
class JobStats(object):
	def __init__(self, jenkins, jobs):
		self.jenkins = jenkins
		self.jobs = jobs
	def job_stats(self):
		stats = '{'
		for j in jobs:
			url = "%s/job/%s/lastBuild/buildStatus" % (jenkins, j)
			print "Reading ", url
			url = urlopen(url).geturl()
			stats += "\"%s\": \"%s\"," % (j, re.search('48x48/([^.]+)\.', url).group(1))
		stats += '}'
		return stats

	def to_file():
		stats = job_stats(jenkins, jobs)
		print str(datetime.now()), stats
		with open("statuses.json", "w+") as f: 
			f.write(stats)

class OfflineJobStats(object):
	def job_stats(self):
		return '{"config-provider-model": "blue", "jenkins_main_trunk": "red", "libs_svnkit": "yellow", "plugin-compat-tester": "blue_anime"}'
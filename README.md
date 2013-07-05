build-semaphore
===============

simple dashboard for jenkins builds status monitoring

Usage
===============
After cloning the repo, create a file config.py from config.py.template. Update properties to the actual values.

To run, execute 
```python build_status.py [filename]```

filename is an optional argument which allows to use config files named different from config.py. If not specified, config.py is used as a config file. 

HTTP server is run on port 8000 by default. To change it, add 'port' parameter to the config file.

Status page is then available at [http://localhost:8000/ci-status.html](http://localhost:8000/ci-status.html)

Arduino support 
===============
Prerequisites: 
# [Arduino drivers](http://www.ftdichip.com/Drivers/VCP.htm)
# pyserial module

To enable, edit config file, set 
```
'arduino': True
'arduino_port': <name of the port> (e.g. /dev/tty.usbserial-A900F5S9)
```

Configuration
===============
```
{
	'jenkins': 'https://ci.jenkins-ci.org/', # Url to the jenkins instance
	'jobs': ['config-provider-model', 'jenkins_main_trunk', 'libs_svnkit', 'plugin-compat-tester'], # List of job names to include to the page
	# 'port': 8000 # HTTP server port
	# 'offline': True, # Uncomment to suppress jenkins polling (useful for debug)
	# 'arduino_port': '/dev/tty.usbserial-A900F5S9', # Port for arduino semaphore
	# 'arduino': False # enable arduino semaphore
}
```
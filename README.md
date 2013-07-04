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
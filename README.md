build-semaphore
===============

simple dashboard for jenkins builds status monitoring

Usage
===============
After cloning the repo, create a file config.py from config.py.template. Update properties to the actual values.

To run, execute 
```python build_status.py [filename]```

filename is an optional argument which allows to use config files named different from config.py. If not specified, config.py is used as a config file. 

Above starts 2 processes: first reads jenkins jobs statuses and writes results to statuses.json. Second is a simple http server. 
Note that currently it's not possible to run 2 instances of build_status.py simultaneously as the result file is not configurable.

HTTP server is run on port 8000 by default. To change it, add 'port' parameter to the config file.
from paver.easy import *
from paver.setuputils import setup, find_packages

version = '0.1'

setup (
	name='sbbapi',
	version=version,
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	django_module='sbbapi.settings',
)
	
	
@task
@cmdopts([
	('port=', 'p', 'Port for the FCGI Server'),
	('host=', 'H', 'Host for the FCGI Server'),
	('fcgifile=', 'f', 'FCGI File Path'),
	('pidfile=', 'i', 'PID File Path'),
	('initfile=', 'n', 'init.d File Path'),
	('virtualenv=', 'E', 'Virtualenv Dir'),
	('module=', 'm', 'Django Module'),
])
def setup_initscript(options):
	from service.common.setup import setup_initd
	setup_initd(options)
	
	
@task
@cmdopts([
	('fcgifile=', 'f', 'FCGI File Path'),
])
def setup_fcgi(options):
	import os
	from service.common.setup import setup_django_fcgi
	if hasattr(options.setup_fcgi, 'fcgifile'):
		setup_django_fcgi(file_path = os.path.abspath(options.setup_fcgi.fcgifile))
	else:
		setup_django_fcgi()

import os
from setuptools import setup,find_packages

setup(
    name='mas_nitro-python',
	version='1.0',
    author='Citrix NetScler MAS',
    packages=[
		'massrc',
		'massrc.com',
		'massrc.com.citrix',
		'massrc.com.citrix.mas',
        'massrc.com.citrix.mas.nitro',
		'massrc.com.citrix.mas.nitro.datatypes',
        'massrc.com.citrix.mas.nitro.exception',
        'massrc.com.citrix.mas.nitro.resource',
        'massrc.com.citrix.mas.nitro.util',
        'massrc.com.citrix.mas.nitro.service',
        'massrc.com.citrix.mas.nitro.resource.Base',
        'massrc.com.citrix.mas.nitro.resource.config'] + 
        [ os.path.join('massrc.com.citrix.mas.nitro.resource.config', mydir) for mydir in find_packages("massrc/com/citrix/mas/nitro/resource/config")],
	classifiers=[
          'Development Status :: 11.1',
          'Intended Audience :: MAS NITRO API',
          'Programming Language :: Python',
          'Topic :: Software Development :: API',
    ],
    description='Python SDK for MAS Nitro API',    
    install_requires=[
        "requests >= 2.1.0",
    ],
    scripts=[
		'sample/system_session.py',
		'sample/system_version.py'
    ],
)
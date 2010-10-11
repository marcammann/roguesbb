import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "SBB",
    version = "0.0.1",
    author = "Peter Manser, Marc Ammann",
    author_email = "mail@petermanser.ch, marc@partiql.com",
    description = (""),
    license = "Apache License",
    keywords = "sbb api",
    url = "http://partiql.com/lab/sbb",
    packages=['sbbfrontend', 'sbbapi', 'tests'],
    long_description=read('README'),
)
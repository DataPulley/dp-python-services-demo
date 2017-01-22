""" Packaging & deployment script """

import os

from setuptools import setup
from setuptools import find_packages

# Create 'build number' if running from server
if 'BUILD_NUMBER' in os.environ:
    with open('build-number', 'w') as f: f.write(os.environ['BUILD_NUMBER'] + '\n')

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read().rstrip('\n')

setup(
    name='dp-python-services-demo',
    description='Demo endpoint creation for Python',
    url='https://github.com/DataPulley/dp-python-servics-dp-python-services-demo',
    author='Data Pulley',
    author_email='development@datapulley.com',
    license='Other/Proprietary License',
    zip_safe=False,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='data pulley python services demo',
    packages=find_packages(exclude=['tests']),
    package_data={
    },
    test_suite='tests'
)


from setuptools import setup, find_packages
	

setup(
	name='numpy-playground',
	version='1.0.0',
	packages=find_packages(exclude=['test-data']),
	install_requires=['numpy']
)
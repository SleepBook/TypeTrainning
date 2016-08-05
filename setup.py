from setuptools import setup

setup(
	author = 'oar',
	version = '0.1',
	description = 'small tool for type training',
	install_requires = ['nose','getch'],
	packages = ['typer'],
	scripts = ['bin/train'],
	name = 'type_trainer'
	)

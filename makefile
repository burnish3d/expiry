SHELL := /usr/bin/bash

setup: requirements_dev.txt
	python3 -m pip install requirements-dev.txt 

clean:
	rm -rf build
	rm -rf dist
	rm -rf __pycache__
	rm -rf expiry.egg-info

venv: venv/bin/activate 
	source ./venv/bin/activate

build:
	./venv/bin/python3 -m setup.py sdist bdist_wheel
	

venv/bin/activate: requirements-dev.txt
	python3 -m venv venv
	./venv/bin/python3 -m pip install -r requirements-dev.txt


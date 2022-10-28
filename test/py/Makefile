.ONESHELL:

all:
	python3 -m venv .venv
	. .venv/bin/activate
	cd ../../pkg
	python3 -m pip install -e .
	cd ../test/py
	./test.py

clean:
	rm -rf venv .venv

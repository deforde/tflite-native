.ONESHELL:

.PHONY: build

build:
	mkdir -p bin include
	cd build
	docker compose build
	docker compose up

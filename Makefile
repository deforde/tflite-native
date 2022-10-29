.ONESHELL:

.PHONY: build

build:
	mkdir -p bin include
	cd build/linux
	docker compose up

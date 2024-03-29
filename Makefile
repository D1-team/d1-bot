.PHONY: init

init:
	@make down
	@make up
	@make ps
down:
	docker-compose down --volumes --remove-orphan
build:
	docker-compose build
stop:
	docker-compose stop
up:
	docker-compose up -d
ps:
	docker-compose ps
format:
	docker exec -it app python3 -m black .
	docker exec -it app python3 -m isort .
lint:
	docker-compose up -d
	docker exec app python3 -m black . --check
	docker exec app python3 -m isort . --check
	docker exec app python3 -m flake8 . --show-source
	docker exec app python3 -m pylint app src
test:
	docker-compose up -d
	docker exec app python3 -m pytest

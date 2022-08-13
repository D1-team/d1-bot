.PHONY: init

init:
	@make down
	@make up
	@make ps
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
ps:
	docker-compose ps
format:
	docker exec -it app python3 -m black .
	docker exec -it app python3 -m isort .
lint:
	docker exec -it app python3 -m black . --check
	docker exec -it app python3 -m isort . --check
	docker exec -it app python3 -m flake8 . --show-source
	docker exec -it app python3 -m pylint app src
test:
	docker exec -it app python3 -m pytest

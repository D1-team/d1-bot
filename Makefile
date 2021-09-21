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
	docker-compose run --rm app python3 -m black .
	docker-compose run --rm app python3 -m isort .
lint:
	docker-compose run --rm app python3 -m black . --check
	docker-compose run --rm app python3 -m flake8 . --show-source
	docker-compose run --rm app python3 -m pylint app src
test:
	docker-compose run --rm app python3 -m pytest
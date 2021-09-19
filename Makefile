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
	docker-compose run --rm app black .
init:
	docker-compose down -v
	docker-compose up -d --build
	docker-compose exec server flask db upgrade

up:
	docker-compose up -d

stop:
	docker-compose down

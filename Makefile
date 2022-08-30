setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

up:
	docker-compose up -d

down:
	docker-compose down

dev:
	./bin/dev_app

init:
	./bin/cmd init

dbshell:
	docker-compose exec db psql -U raffler

.PHONY: docker-up run-server

db:
	cd docker && docker compose up -d

db-down:
	cd docker && docker compose down

fastapi:
	uvicorn app.main:app
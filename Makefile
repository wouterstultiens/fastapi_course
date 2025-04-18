.PHONY: docker-up run-server

db:
	cd docker && docker compose up -d

fastapi:
	uvicorn app.main:app
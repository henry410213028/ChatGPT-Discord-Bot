VENV_PREFIX=poetry run

.PHONY: install run test docs

install:
	pip install poetry && poetry install

lint:
	$(VENV_PREFIX) black . --check
	$(VENV_PREFIX) isort --profile black --check-only .
	$(VENV_PREFIX) flake8 .
	$(VENV_PREFIX) mypy src/ tests/

format:
	$(VENV_PREFIX) black .
	$(VENV_PREFIX) isort --profile black .

coverage:
	PYTHONPATH=./src $(VENV_PREFIX) pytest --cov=src ./tests/

deps:
	poetry export -f requirements.txt -o requirements.txt --without-hashes

deps-dev:
	poetry export -f requirements.txt -o requirements-dev.txt --without-hashes --dev

test:
	PYTHONPATH=./src $(VENV_PREFIX) pytest ./tests/

build:
	docker-compose build

deploy:
	docker-compose up -d

down:
	docker-compose down

run:
	$(MAKE) build && $(MAKE) down && $(MAKE) deploy
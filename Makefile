install:
	poetry install

build:
	poetry build

update:
	poetry update

lint:
	poetry run flake8
	poetry run mypy -p pystepikconnect

publish:
	poetry publish --dry-run

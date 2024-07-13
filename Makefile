install:
	poetry install

build:
	poetry build

update:
	poetry update

lint:
	poetry run flake8
	poetry run mypy -p pystepikconnect

fix:
	poetry run black pystepikconnect

publish:
	poetry publish --dry-run

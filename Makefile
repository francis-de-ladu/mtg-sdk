SHELL = /usr/bin/env bash
SRC_PATH = src/

static-fix: black isort flake8

black:
	poetry run black $(SRC_PATH)

isort:
	poetry run isort $(SRC_PATH)

flake8:
	poetry run flake8 $(SRC_PATH) --max-line-length=120 --max-complexity=10

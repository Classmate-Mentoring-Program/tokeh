.PHONY: install test lint format notebook

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

lint:
	ruff check tokeh/ tests/

format:
	black tokeh/ tests/

notebook:
	jupyter notebook notebooks/

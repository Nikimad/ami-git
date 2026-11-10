test:
	python -m uv run pytest -v

lint:
	python -m uv run ruff check .

format:
	python -m uv run ruff format .

check: lint test
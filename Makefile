test:
	python -m uv run pytest -v

lint:
	python -m uv run ruff check .

format:
	python -m uv run ruff format .

typecheck:
	python -m uv run mypy

check: lint typecheck test
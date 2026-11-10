# git-training

Маленькая консольная программа для подсчёта статистики и учебное задание по git: слияние веток и разрешение конфликта.

```
$ uv run statscli max 1 2 3
3
$ uv run statscli avg 1 2 3
2.0
```

## Требования

- Git
- [uv](https://docs.astral.sh/uv/) (он сам поставит нужный Python и зависимости)
- make (необязательно, всё то же самое можно запустить командами из таблицы ниже)

## Быстрый старт

```bash
git clone <url> ami-git
cd ami-git
uv sync
uv run statscli --help
```

## Команды

| Что сделать | Через make | Без make |
|---|---|---|
| Тесты | `make test` | `uv run pytest -v` |
| Линтер | `make lint` | `uv run ruff check .` |
| Форматирование | `make format` | `uv run ruff format .` |
| Типы | `make typecheck` | `uv run mypy` |
| Всё сразу | `make check` | цепочка из команд выше |

## Структура

```
src/statscli/
├── cli.py       # разбор аргументов (argparse)
├── stats.py     # вычисления: average, maximum, minimum
└── __main__.py  # запуск через python -m statscli
tests/
└── test_stats.py
```
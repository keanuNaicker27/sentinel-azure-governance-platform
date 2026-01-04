.PHONY: setup test chaos lint

setup:
	bash scripts/bootstrap_env.sh

test:
	pytest tests/unit tests/integration

chaos:
	python scripts/simulation/chaos_monkey.py --type drift
	pytest tests/integration/test_bc_to_sql_pipeline.py

lint:
	pylint sentinel/
	sqlfluff lint sql/ --dialect snowflake

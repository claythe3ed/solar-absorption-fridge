.PHONY: install run test clean

install:
	pip install -r requirements.txt

run:
	python src/main.py

test:
	pytest tests/

clean:
	rm -rf __pycache__ .pytest_cache

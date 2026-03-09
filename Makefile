
install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 src/

run:
	python -m src.scanner app.apk

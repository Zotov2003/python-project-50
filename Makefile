install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 hexlet_code

check:
	poetry run flake8 hexlet_code
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report=xml
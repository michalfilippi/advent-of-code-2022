.PHONY: test black mypy flake8 all

test:
	cd src; python -m pytest ../tests

black:
	black src tests

mypy:
	mypy src tests

flake8:
	flake8 src tests

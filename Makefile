# * Makefile

# * Here you can write custom scripts!
# * You can run one or multiple scripts at once

PYTHON_VERSION = 3.12.1
.PHONY: help

# * Install all python dependencies
setup:
	poetry install
	@python3 machine_learning/utils/ui/setup.py; \
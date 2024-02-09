# * Makefile

# * Here you can write custom scripts!
# * You can run one or multiple scripts at once

PYTHON_VERSION = 3.12.1
.PHONY: help

# * Help target to display all available targets
help:
	@awk 'BEGIN {command = ""; desc = ""} /^# \* / {if (command != "") print command ": " desc; desc = $$0; gsub(/^# \* /, "", desc); command = ""} /^[a-zA-Z_-]+:/ {command = $$0; gsub(/:.*/, "", command)} END {if (command != "") print command ": " desc}' $(MAKEFILE_LIST)


# * Install all python dependencies
setup:
	poetry install
	@python3 machine_learning/utils/ui/setup.py; \


# * Run E2E tests
test:
	@python3 machine_learning/utils/ui/before_tests.py
	@pytest && python3 machine_learning/utils/ui/finished_tests.py || python3 machine_learning/utils/ui/failed_tests.py

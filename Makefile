# Variables
CC = gcc

# The shell command spawns a shell, according to the $SHELL environment variable, within the virtual environment. If one doesn’t exist yet, it will be created.
# As such, exit should be used to properly exit the shell and the virtual environment instead of deactivate.
activate-venv:
	poetry shell

use-python:
	# pyenv for windows and macos users
	pyenv install 3.9.8
	pyenv local 3.9.8  # Activate Python 3.9 for the current project
	poetry install

# Lint all files in the current directory.
.PHONY: ruff-check
ruff-check:
	ruff check ./app

.PHONY: ruff-format
ruff-format:
	ruff format ./app  # Format all files in the current directory.

#This command exports the lock file to other formats.
requirements-export:
	poetry export -f requirements.txt --output requirements.txt

#The install command reads the pyproject.toml file from the current project, resolves the dependencies, and installs them.
pip-setup:
	poetry install  --without dev

VENV=venv
VENV_PATH=""

ifeq ($(OS), Windows_NT)
	PYTHON=py
else
	PYTHON=python
endif

init: ${VENV}


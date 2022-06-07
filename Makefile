VENV=venv

init: ${VENV}
	source venv/bin/activate && pip install -r requirements.txt

${VENV}:
	python -m venv ${VENV}

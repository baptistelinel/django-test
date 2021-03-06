install_requirements:
	pip install -r requirements.txt

format:
	yapf -i -r github/ qwarry/ --style='{based_on_style: pep8, indent_width: 4}'

unit_tests:
	PYTHONPATH=github pytest github/tests/unit_tests

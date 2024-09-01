PACKAGE_NAME = diem
PYTHON_VIRTUALENV_PATH = .venv

venv:
	@if [ ! -d $(PYTHON_VIRTUALENV_PATH) ]; then \
		python3 -m venv $(PYTHON_VIRTUALENV_PATH); \
		echo "$(COLOR_YELLOW)Created a python virtual environment at path: $(PYTHON_VIRTUALENV_PATH)$(COLOR_RESET)"; \
	fi

clean_venv:
	@if [ -d $(PYTHON_VIRTUALENV_PATH) ]; then \
		rm -rf $(PYTHON_VIRTUALENV_PATH); \
		echo "$(COLOR_YELLOW)Removed python virtual environment at path: $(PYTHON_VIRTUALENV_PATH)$(COLOR_RESET)"; \
	fi

package:
	@. $(PYTHON_VIRTUALENV_PATH)/bin/activate && \
	pip install poetry && \
	poetry install; \

	@if [ -d .git ]; then \
		poetry run autohooks activate && \
		poetry run autohooks check; \
	fi

clean_package:
	@. $(PYTHON_VIRTUALENV_PATH)/bin/activate && \
	pip uninstall -y $(PACKAGE_NAME)

all: venv package

clean: clean_package

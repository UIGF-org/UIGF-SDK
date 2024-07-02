# Makefile for Python project

# 定义变量
PYTHON := python
PMPT := python -m pmpt
PIP := pip
VENV := venv

# 定义目录
DIST_DIR := dist
BUILD_DIR := build

# 定义目标
ALL: help
help:
	@echo "Available targets:"
	@echo "  build         Build Package"
	@echo "  init           Initialization"
	@echo "  clean         Clean up"
	@echo "  cleanall       Clear All"
	@echo "  venv          Create a virtual environment"

build: pre
	$(PYTHON) setup.py bdist_wheel -d $(DIST_DIR) sdist -d $(DIST_DIR) bdist_egg -d $(DIST_DIR) 
	
init: 
	@for file in requirements/*.txt; do \
		if [ -f "$$file" ]; then \
			$(PIP) install -r  "$$file"; \
		fi; \
	done
	
venv:
	$(PYTHON) -m venv $(VENV)

cleanall: clean
	rm -r $(VENV)
	
clean:
	rm -r $(DIST_DIR) $(BUILD_DIR) pmpt.egg-info

commit:
	@if [ -z "$(msg)" ]; then \
		echo "Please provide a commit message using 'msg' parameter."; \
		exit 1; \
	else \
		git add .; \
		git commit -m "$(msg)"; \
	fi
	
pre: init
	$(PYTHON) -m black .

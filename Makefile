.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist

help:
	@echo "Usage:"
	@echo ""
	@echo "make <command>"
	@echo ""
	@echo "Building"
	@echo "--------"
	@echo ""
	@echo "docs: generate documentation in docs/_build/html"
	@echo "clean: restores code tree to a clean state"
	@echo ""
	@echo "Development"
	@echo "-----------"
	@echo ""
	@echo "lint: check Python style with flake8"

clean:
	$(MAKE) -C docs clean

lint:
	$(MAKE) -C docs linkcheck

docs: clean
	$(MAKE) -C docs html

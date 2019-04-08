.DEFAULT_GOAL := help

RUNTEST=python3 -m unittest
RUNMAIN= python3 main.py

# All .py files inside each module name
# https://www.gnu.org/software/make/manual/html_node/Wildcard-Function.html
ALL_ERROR_MODULES=$(wildcard error/*.py)
ALL_LEXER_MODULES=$(wildcard lexer/*.py)
ALL_MEMORY_MODULES=$(wildcard memory/*.py)
ALL_PARSER_MODULES=$(wildcard parser/*.py)
ALL_QUADRUPLE_MODULES=$(wildcard quadruple/*.py)
ALL_ROOT_MODULES=$(wildcard *.py)
ALL_SEMANTIC_CUBE_MODULES=$(wildcard semantic_cube/*.py)
ALL_STACK_MODULES=$(wildcard stack/*.py)
ALL_TEST_MODULES=$(wildcard tests/test_*.py)

ALL_MODULES=$(ALL_ERROR_MODULES) $(ALL_LEXER_MODULES) $(ALL_MEMORY_MODULES) $(ALL_PARSER_MODULES) $(ALL_QUADRUPLE_MODULES) $(ALL_ROOT_MODULES) $(ALL_SEMANTIC_CUBE_MODULES) $(ALL_STACK_MODULES) $(ALL_TEST_MODULES)

# Path from all .tl files (inside our_tests)
ALL_TL_FILES=$(wildcard our_tests/*.tl)
# Names from all .tl files (inside our_tests)
ALL_TL_FILENAMES=$(patsubst our_tests/%, %, $(wildcard our_tests/*.tl))

ALL_OBJECT_FILES=$(wildcard object_code/*.obj)

help: ##Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean: ##Removes generated files (eg. .obj)
	@echo 'Clean triggered'
	@echo ${ALL_OBJECT_FILES}
	@rm -r ${ALL_OBJECT_FILES}


format: ##Applies BLACK to all py files in defined modules.
	@echo 'Format triggered'
	@black ${ALL_MODULES}

##prepare: Applies FORMAT TEST.
prepare: format clean run test

run: ##Run all .tl files
	${RUNMAIN} ${ALL_TL_FILES}

show: ##Show all .tl files
	@echo ${ALL_TL_FILENAMES}

test: ##Run all automated tests (unnitest framework).
	@echo 'Test triggered'
	${RUNTEST} ${ALL_TEST_MODULES}

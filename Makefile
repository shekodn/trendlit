APP=trendlit
PROJECT=github.com/shekodn/trendlit
RELEASE?=0.0.14

COMMIT?=$(shell git rev-parse HEAD)
BUILD_TIME?=$(shell date -u '+%Y-%m-%d_%H:%M:%S')

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
ALL_RUNTIME_MEMORY_MODULES=$(wildcard *.py)
ALL_SEMANTIC_CUBE_MODULES=$(wildcard semantic_cube/*.py)
ALL_SERVER_MODULES=$(wildcard server/*.py)
ALL_STACK_MODULES=$(wildcard stack/*.py)
ALL_TEST_MODULES=$(wildcard tests/test_*.py)
ALL_TRENDLIT_MODULES=$(wildcard trendlit_helper/*.py)
ALL_VIRTUAL_MACHINE_MODULES=$(wildcard tests/test_*.py)

ALL_MODULES=$(ALL_ERROR_MODULES) $(ALL_LEXER_MODULES) $(ALL_MEMORY_MODULES) $(ALL_PARSER_MODULES) $(ALL_QUADRUPLE_MODULES) $(ALL_ROOT_MODULES) $(ALL_RUNTIME_MEMORY_MODULES) $(ALL_SEMANTIC_CUBE_MODULES) $(ALL_SERVER_MODULES) $(ALL_STACK_MODULES) $(ALL_TEST_MODULES) $(ALL_TRENDLIT_MODULES) $(ALL_VIRTUAL_MACHINE_MODULES)

# Path from all .tl files (inside our_tests)
ALL_TL_FILES=$(wildcard our_tests/*.tl)
# Names from all .tl files (inside our_tests)
ALL_TL_FILENAMES=$(patsubst our_tests/%, %, $(wildcard our_tests/*.tl))

ALL_OBJECT_FILES=$(wildcard object_code/*.obj)
ALL_COMPILED_FILES=$(wildcard compiled_code/*.html)
ALL_COMPILED_TEST_FILES=$(wildcard compiled_code_test/*.html)

# List all running containers
ALL_DOCKER_CONTAINERS=$(shell docker ps -aq)

build:## Spins that beautiful container!
	@./scripts/docker_build.sh

bump:## Bumps version
	@./bump_version.sh

check:## Check if the tag that is going to be pushed is unique. In other words, if RELEASE variable was updated in the Makefile.
	@./scripts/docker_check.sh

clean: ##Removes generated files (eg. .obj and .html)
	@echo 'Clean triggered'
	@echo 'Removing object code (obj)'
	@echo ${ALL_OBJECT_FILES}
	@rm -r ${ALL_OBJECT_FILES}
	@echo 'Removing compiled test file'
	@echo ${ALL_COMPILED_TEST_FILES}
	@rm -r ${ALL_COMPILED_TEST_FILES}
	@echo 'Removing compiled code (html)'
	@echo ${ALL_COMPILED_FILES}
	@rm -r ${ALL_COMPILED_FILES}


format: ##Applies BLACK to all py files in defined modules.
	@echo 'Format triggered'
	@black ${ALL_MODULES}

help: ##Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

##prepare: Applies format clean trendlit test
prepare: format trendlit test clean

push: ## Push docker image to docker hub
	@./scripts/docker_push.sh

machine: ##If Docker compose is up, it goes into the container
	@echo 'Machine triggered'
	@docker exec -it cgi bash

rmi:## Removes docker image
	@./scripts/docker_rmi.sh

run:## Run latest built
	@echo 'Run triggered'
	@./scripts/docker_run.sh

show: ##Show all .tl files
	@echo ${ALL_TL_FILENAMES}

stop: ### Stop all running containers
	@echo "The following containers will be stopped"
	@echo ${ALL_DOCKER_CONTAINERS}
	@docker stop $(ALL_DOCKER_CONTAINERS)

trendlit: ##Run all .tl files
	${RUNMAIN} ${ALL_TL_FILES}

test: ##Run all automated tests (unnitest framework).
	@echo 'Test triggered'
	${RUNTEST} ${ALL_TEST_MODULES}

version: ##Prints current version
	@echo -n ${RELEASE}
	@echo

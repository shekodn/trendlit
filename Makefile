RUNTEST=python3 -m unittest
RUNMAIN= python3 main.py

ALL_TRENDLIT_MODULES=$(patsubst %.py, %.py, $(wildcard our_tests/test_*.py))
ALL_TEST_MODULES=$(patsubst %.py, %.py, $(wildcard tests/test_*.py))

# RUN 'make' before commiting to make sure anything broke during our changes
default:
	make run
	make test

# TODO Run all trendlit_tests inside OUR_TESTS directory. Currently it only runs the first argument
run:
	${RUNMAIN} ${ALL_TRENDLIT_MODULES}
% : test_%.py
	${RUNMAIN} test_$@

# Runs all tests (unnitest framework) inside TESTS directory
test:
	${RUNTEST} ${ALL_TEST_MODULES}
% : test_%.py
	${RUNTEST} test_$@

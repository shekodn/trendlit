RUNTEST=python3 -m unittest
RUNMAIN= python3 main.py

ALL_TRENDLIT_MODULES=$(patsubst %.tl, %.tl, $(wildcard our_tests/test_*.tl))
ALL_TEST_MODULES=$(patsubst %.py, %.py, $(wildcard tests/test_*.py))

# RUN 'make' before commiting to make sure anything broke during our changes
default:
	make run  && make test

# TODO Run all trendlit_tests inside OUR_TESTS directory. Currently it only runs the first argument

run:
	${RUNMAIN} our_tests/test_sample_code.tl
	${RUNMAIN} our_tests/test_many_declared_local_vars.tl
# ${RUNMAIN} ${ALL_TRENDLIT_MODULES} This should produce the tests for everything
# TODO find a cleaner solution
# % : test_%.tl
# 	${RUNMAIN} test_$@

# Runs all tests (unnitest framework) inside TESTS directory
test:
	${RUNTEST} ${ALL_TEST_MODULES}
# % : test_%.py
# 	${RUNTEST} test_$@

RUNTEST=python3 -m unittest
# RUNMAIN= python3 main.py our_tests/sample_code.html.py
RUNMAIN= python3 main.py

ALL_TRENDLIT_MODULES=$(patsubst %.py, %.py, $(wildcard our_tests/test_*.py))


ALL_TEST_MODULES=$(patsubst %.py, %.py, $(wildcard tests/test_*.py))

default:
	make run
	make test

run:
	${RUNMAIN} ${ALL_TRENDLIT_MODULES}
% : test_%.py
	${RUNMAIN} test_$@


test:
	${RUNTEST} ${ALL_TEST_MODULES}
% : test_%.py
	${RUNTEST} test_$@

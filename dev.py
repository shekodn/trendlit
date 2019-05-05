#!/usr/bin/python3
import sys
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh
from trendlit_helper.trendlit_helper import TrendlitHelper

trendlit_helper = TrendlitHelper()

if __name__ == "__main__":

    file = sys.argv[1]

    if len(file) > 0:
        dir = "compiled_code/"
        trendlit_helper.reads_file(dir, file)
    else:
        print("File missing")

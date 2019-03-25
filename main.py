#!/usr/bin/python3
import sys
from parser.parser import parser, yacc
from semantic_cube.semantic_cube import (
    Cube,
    type_int,
    type_double,
    type_bool,
    type_error,
    type_none,
)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, "r")
            data = f.read()
            f.close()
            yacc.parse(data, tracking=True)
        except EOFError:
            print("EOFError")
    else:
        print("File missing")
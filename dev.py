#!/usr/bin/python3
import sys
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine import run_code

if __name__ == "__main__":

    file = sys.argv[1]

    if len(file) > 0:

        print("Attempting to compile the following file:")
        print(f"{file}\n")

        try:
            f = open(file, "r")
            data = f.read()
            f.close()
            yacc.parse(data, tracking=True)
            if error_helper.error_cont is 0:
                print(f"{file} compiles!\n")
                _, file_name = file.split("/")
                quad_helper.print_to_file(f"object_code/{file_name}.obj")
                run_code(quad_helper.queue_quad, memory.constant_values)
            else:
                print(f"{file} does not compile. Please try harder")
                print(f"Number of errors: {error_helper.error_cont}")
                error_helper.print_errors()
            error_helper.reset()
            quad_helper.reset()
            parser_helper.reset()
            memory.reset()
            print("--------------------------------------------")

        except EOFError:
            print("EOFError")
    else:
        print("File missing")

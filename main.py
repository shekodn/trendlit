#!/usr/bin/python3
import sys
from parser.parser import parser, yacc, procedure_directory, quad_helper, error_helper

if __name__ == "__main__":

    files = sys.argv[1:]

    if len(files) > 0:

        print("Attempting to compile the following files:")
        print(f"{files}\n")

        for file in files:
            try:
                f = open(file, "r")
                data = f.read()
                f.close()
                yacc.parse(data, tracking=True)

                if error_helper.error_cont is 0:
                    print(f"{file} compiles!\n")
                    _, file_name = file.split("/")
                    quad_helper.print_to_file(f"object_code/.{file_name}.obj")
                else:
                    print(f"{file} does not compile. Please try harder")
                    print(f"Number of errors: {error_helper.error_cont}")
                    error_helper.print_errors()
                error_helper.reset()
                quad_helper.reset()
                print("--------------------------------------------")

            except EOFError:
                print("EOFError")
    else:
        print("File missing")

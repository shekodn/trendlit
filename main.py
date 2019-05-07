#!/usr/bin/python3
import sys
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code

if __name__ == "__main__":
    """
        Description: Main module calls and handles all other modules, libraries and classes used during compilation and execution.
            The main module is in charge of the overall flow of the compilation process. This module is primarily used in the server that
            runs the trendlit cloud based compiler.
        Params:
        Return:
    """
    files = sys.argv[1:]

    if len(files) > 0:

        print("Attempting to compile the following files:")
        print(f"{files}\n")

        for file in files:
            try:
                # Read the .tl input file that contains trendlit code
                f = open(file, "r")
                data = f.read()
                f.close()
                try:
                    yacc.parse(data, tracking=True)
                    if error_helper.error_cont is 0:
                        # No errors were found during compilation
                        print(f"{file} compiles!\n")
                        _, file_name = file.split("/")
                        # Generate the obj file with the quadruples generated during compilation
                        quad_helper.print_to_file(f"object_code/{file_name}.obj")
                        # Start execution in the Virtual Machine (send quads and constants)
                        run_code(quad_helper.queue_quad, memory.constant_values)
                    else:
                        # Could not compile successfully
                        print(f"{file} does not compile. Please try harder")
                        # Pretty print all errors collected during compilation
                        print(f"Number of errors: {error_helper.error_cont}")
                        error_helper.print_errors()
                except:
                    # If program exists because of an unexpected crash/error, then catch the error and pretty print
                    print(f"{file} couldn't compile successfully.\n")

                # Reset all compilation and execution environments
                # Resetting is useful for testing several files (no overlapped results)
                error_helper.reset()
                quad_helper.reset()
                parser_helper.reset()
                memory.reset()
                print("--------------------------------------------")

            except EOFError:
                print("EOFError")
    else:
        # Catch a not found file error
        print("File missing")

#!/usr/bin/python3
import sys
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh


class TrendlitHelper(object):
    def reads_file(self, dir, file):
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
                vmh.print_to_file(f"{dir}/{file_name}.html")
            else:
                print(f"{file} does not compile. Please try harder")
                print(f"Number of errors: {error_helper.error_cont}")
                error_helper.print_errors()
            error_helper.reset()
            quad_helper.reset()
            parser_helper.reset()
            memory.reset()
            vmh.reset()
            print("--------------------------------------------")
        except EOFError:
            print("EOFError")

    def run(self, data):
        try:
            yacc.parse(data, tracking=True)

            if error_helper.error_cont is 0:
                run_code(quad_helper.queue_quad, memory.constant_values)
                for result in vmh.queue_results:
                    print(result)
            else:
                print(f"Your code doesn't compile. Please try harder \n")
                print(f"# of Errors: {error_helper.error_cont}\n")
                error_helper.print_errors()
        except:
            error = f"Error. We couldn't compile successfully.\n"
            print(error)

#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys, os
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue("textcontent"):
    text_content = form.getvalue("textcontent")
else:
    text_content = "Nein!"

print("Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title> Trendlit - Cloud Based Programming Language</title>")
print("</head>")

data = text_content

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

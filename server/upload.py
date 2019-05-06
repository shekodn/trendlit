#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys, os
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh
from trendlit_helper.trendlit_helper import TrendlitHelper

trendlit_helper = TrendlitHelper()


cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form["filename"]

print(f"Content-type:text/html\n")

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open("/tmp/" + fn, "wb").write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully\n'
    with open("/tmp/" + fn, "r") as file:
        data = file.read()
    trendlit_helper.run(data)
else:
    message = "No file was uploaded\n"
    print(message)

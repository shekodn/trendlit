#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys, os
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh
from trendlit_helper.trendlit_helper import TrendlitHelper

trendlit_helper = TrendlitHelper()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from text area field
if form.getvalue("textcontent"):
    text_content = form.getvalue("textcontent")
else:
    text_content = "Nein!"
# Get data from radio button fields
if form.getvalue("type"):
    # html or plain
    type = form.getvalue("type")
else:
    type = "html"

print(f"Content-type:text/{type}\n")

data = text_content

try:
    trendlit_helper.run(data)
except:
    print("Uknown error.")

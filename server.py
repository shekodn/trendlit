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
    # for debugging
    # text_content = "program the_name_of_the_program script { eval(7 + 1) }"


print("Content-type:text/html\n")
# print ("<html>")
# print ("<head>")
# print ("<title> Trendlit - Cloud Based </title>")
# print ("</head>")


path = "/tmp/"
tl_file_name = "main.tl"
compiled_file = "trendlit.tl"


data = text_content


# data = ("""
#  %s
# """ % (data))
# data = data.rstrip()

# data = """
# # Don't move, otherwise the TEST will break
#
#
# program the_name_of_the_program
#
#     script {
#       int A
#       int B
#       int C
#       int D = 1
#       int E
#       bool F
#       str G
#       double H
#       eval(A)
#       eval(1)
#       eval(True)
#       eval(A + B)
#       eval(A > B)
#     }
# """
# data = data.rstrip()
#
# # with open(tl_file_name, 'w') as filetowrite:
# #     filetowrite.write(text_content)
# #     filetowrite.close()
#
#
#     # f = open(tl_file_name, "r")
#     # data = f.read()
#     # f.close()
#     # data = unicode(text_content, "utf-8")
#


# data = """program the_name_of_the_program
#
#     script {
#         eval(1 + 9)
#     }
# """
# data.replace('', '\n')
# data.replace(' ', '\n')
data.replace("\n", " ")

# print(len(data))
data = data.rstrip()
#
# print(len(data))
data = data.strip()


try:
    yacc.parse(data, tracking=True)

    if error_helper.error_cont is 0:
        run_code(quad_helper.queue_quad, memory.constant_values)
        for result in vmh.queue_results:
            print(result)
    else:
        error = f"{tl_file_name} does not compile. Please try harder \n"
        number_of_errors = f"# of Errors: {error_helper.error_cont}\n"
        error_output = error + number_of_errors

        print(error_output)
except:
    error = f"{tl_file_name} couldn't compile successfully.\n"
    print(error)

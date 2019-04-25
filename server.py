#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys, os
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine import run_code


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered YET"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Text Area - Fifth CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> Entered Text Content is %s</h2>" % text_content)
print ("</body>")


tl_file_name = "main.tl"

# with open(tl_file_name, 'w') as filetowrite:
#     filetowrite.write(text_content)
#     filetowrite.close()

try:
    f = open(tl_file_name, "r")
    data = f.read()
    f.close()
    try:
        yacc.parse(data, tracking=True)
        if error_helper.error_cont is 0:
            print(f"{tl_file_name} compiles!\n")
            # _, file_name = file.split("/")
            # quad_helper.print_to_file(f"object_code/{file_name}.obj")
            run_code(quad_helper.queue_quad, memory.constant_values)
        else:
            print(f"{tl_file_name} does not compile. Please try harder")
            print(f"Number of errors: {error_helper.error_cont}")
            error_helper.print_errors()
    except:
        print(f"{tl_file_name} couldn't compile successfully.\n")

    error_helper.reset()
    quad_helper.reset()
    parser_helper.reset()
    memory.reset()
    print("--------------------------------------------")

except EOFError:
    print("EOFError")







# file_name = "trendlit.html"
# exists = os.path.exists(file_name)    # True
#
# if (exists is True):
#     try:
#         f = open(file_name, "r")
#         data = f.read()
#         f.close()
#         yacc.parse(data, tracking=True)
#         error_helper.reset()
#         quad_helper.reset()
#         parser_helper.reset()
#         return number_of_errors
#     except EOFError:
#         print("EOFError")
#
#
#
#
#
#
#
# if (exists is True):
#
#     with open(file, 'w') as filetowrite:
#     filetowrite.write(text_content)
#     filetowrite.close()
#
#
#     f = open(file_name, 'r')
#
#     # To get everything in the file, just use read()
#     file_contents = f.read()
#
#     # And to print the contents, just do:
#     print (file_contents)
#
#     # Don't forget to close the file when you're done.
#     f.close()
#
#
# else:
#     print(f"file {file_name} doesn't exist")
#
#
#
# files = []
# # = sys.argv[1:]
#
# if len(files) > 0:
#
#     print("Attempting to compile the following files:")
#     print(f"{files}\n")
#     #
#     # for file in files:
#     #     try:
#     #         f = open(file, "r")
#     #         data = f.read()
#     #         f.close()
#     #         try:
#     #             yacc.parse(data, tracking=True)
#     #             if error_helper.error_cont is 0:
#     #                 print(f"{file} compiles!\n")
#     #                 _, file_name = file.split("/")
#     #                 quad_helper.print_to_file(f"object_code/{file_name}.obj")
#     #                 run_code(quad_helper.queue_quad, memory.constant_values)
#     #             else:
#     #                 print(f"{file} does not compile. Please try harder")
#     #                 print(f"Number of errors: {error_helper.error_cont}")
#     #                 error_helper.print_errors()
#     #         except:
#     #             print(f"{file} couldn't compile successfully.\n")
#     #
#     #         error_helper.reset()
#     #         quad_helper.reset()
#     #         parser_helper.reset()
#     #         memory.reset()
#     #         print("--------------------------------------------")
#     #
#     #     except EOFError:
#     #         print("EOFError")
# else:
#     print("File missing")

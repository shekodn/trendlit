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
   text_content = "Nein!"
   # for debugging
   # text_content = "program the_name_of_the_program script { eval(7 + 1) }"


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title> Trendlit - Cloud Based </title>")
print ("</head>")

print ("<body>")


tl_file_name = "main.tl"
compiled_file = "trendlit.tl"



# with open(tl_file_name, 'w') as filetowrite:
#     filetowrite.write(text_content)
#     filetowrite.close()


try:
    # f = open(tl_file_name, "r")
    # data = f.read()
    # f.close()
    data = text_content
    try:
        yacc.parse(data, tracking=True)
        if error_helper.error_cont is 0:
            print(f"{tl_file_name} compiles!\n")
            run_code(quad_helper.queue_quad, memory.constant_values)
            os.chmod(compiled_file, 0o644)
            with open(compiled_file) as file:
                content = file.read()
                print(content)
        else:
            error = f"{tl_file_name} does not compile. Please try harder \n"
            number_of_errors = f"# of Errors: {error_helper.error_cont}\n"
            error_output = error + number_of_errors

            print(error_output)
    except:
        error = f"{tl_file_name} couldn't compile successfully.\n"
        print(error)

except EOFError:
    print("EOFError")

print ("</body>")

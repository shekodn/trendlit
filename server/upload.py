#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys, os
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh


cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form["filename"]

print(f"Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title> Trendlit - Cloud Based Programming Language</title>")
print("</head>")
print("<body>")

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open("/tmp/" + fn, "wb").write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully\n'

    try:
        with open("/tmp/" + fn, "r") as file:
            data = file.read()

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
        message = f"Error. We couldn't compile successfully.\n"
        print(message)
else:
    message = "No file was uploaded\n"
    print(message)


print("</body>")
print("</html>")

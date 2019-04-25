#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Text Area - Fifth CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> Entered Text Content is %s</h2>" % text_content)
print ("</body>")




files = []
# = sys.argv[1:]

if len(files) > 0:

    print("Attempting to compile the following files:")
    print(f"{files}\n")
    #
    # for file in files:
    #     try:
    #         f = open(file, "r")
    #         data = f.read()
    #         f.close()
    #         try:
    #             yacc.parse(data, tracking=True)
    #             if error_helper.error_cont is 0:
    #                 print(f"{file} compiles!\n")
    #                 _, file_name = file.split("/")
    #                 quad_helper.print_to_file(f"object_code/{file_name}.obj")
    #                 run_code(quad_helper.queue_quad, memory.constant_values)
    #             else:
    #                 print(f"{file} does not compile. Please try harder")
    #                 print(f"Number of errors: {error_helper.error_cont}")
    #                 error_helper.print_errors()
    #         except:
    #             print(f"{file} couldn't compile successfully.\n")
    #
    #         error_helper.reset()
    #         quad_helper.reset()
    #         parser_helper.reset()
    #         memory.reset()
    #         print("--------------------------------------------")
    #
    #     except EOFError:
    #         print("EOFError")
else:
    print("File missing")

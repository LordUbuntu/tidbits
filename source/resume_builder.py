#!/bin/python3
# Created by Jacobus Burger (2022)
# Info:
#   This is a python script I wrote to automate a resume workflow.
#   It's useful enough to become it's own project maybe.
#   It works by taking a markdown file to start,
#    then converts that into an html file,
#    then uses the html and a css file to render
#    faithful imitations of the html file used.
#   This is done using
#   - pypandoc to convert markdown into html
#   - weasyprint to apply css stylings to the html and produce pdf
# assumptions:
# css file will have same name as html file
# output file will always be pdf
from pypandoc import convert_file as convert
from weasyprint import HTML, CSS
from sys import argv
from pathlib import Path

if len(argv) <= 1:
    quit("no markdown or html file selected")
else:
    _in = argv[1]
    _out = Path(_in).stem + ".pdf"
print(_in, _out)


# if input is markdown file, then generate html file with same stem name
if Path(_in).suffix == ".md":
    convert(_in, "html5", outputfile=(Path(_in).stem + ".html"))
# if input is html file, then generate pdf with css
elif Path(_in).suffix == ".html":
    html = HTML(Path(_in).stem + ".html")
    Path(Path(_in).stem + ".css").touch()
    css = CSS(Path(_in).stem + ".css")
    html.write_pdf(_out, stylesheets=[css])
# complain in all other cases
else:
    quit("file extension is not md or html")

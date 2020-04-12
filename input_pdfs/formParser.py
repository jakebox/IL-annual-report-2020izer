###
### Form Parser by Jake Boxerman (c) 2019
### Takes in source PDF and exports each form data into CSV and
### removes first line.
###

import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

year = "2020"
this_year = "2019"
form_to_fill = "blank_form.pdf"

filename = str(sys.argv[1])
output_csv_filename = filename.replace('pdf', 'csv').replace('2019', year)

fp = open(filename, 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
fields = resolve1(doc.catalog['AcroForm'])['Fields']

file = open(output_csv_filename, 'w')
counter = -2 # For writing out line numbers

for i in fields:
    field = resolve1(i)
    name, value = field.get('T'), field.get('V')
    ''' Lines with content start with a 'b', so we use that to check if there is
    data to be taken. Data is then formatted to it is in 3rd column of CSV with 
    proper column number in first column. '''
    if str(value)[0] == "b":
        counter += 1
        if counter == 2:
            date = str(value).replace("2019", "2020")
            file.write(str(counter) + ", " + "n/a," + '"' + str(date)[1:] + '",' + "\n")
        elif counter == 3: # Updating year
            file.write(str(counter) + ", " + "n/a," + '"' + year + '",' + "\n")
        elif counter == 20 or counter == 26: # Updating year again
            date = str(value).replace("2018", this_year)
            file.write(str(counter) + ", " + "n/a," + '"' + str(date)[1:] + '",' + "\n")
        else:
            file.write(str(counter) + ", " + "n/a," + '"' + str(value)[1:] + '",' + "\n")
    else:
        counter += 1
        if counter == 37:
            file.write(str(counter) + ", " + "n/a," + '"' + "Yes" + '",' + "\n") # Checking Box 10b

file.close()

with open(output_csv_filename, 'r') as fin: # Read in the file
    data = fin.read().splitlines(True) # Makes file content a list
with open(output_csv_filename, 'w') as fout: # Writing out the lines from the file, with a change
    fout.write('"' + form_to_fill + '"' + ",ignored,data,blank\n") # Adds CSV top line with pdf filename to be used with Pdfforms
    data = iter(data) # Turns the list into an iterator object (seems faster? not sure)
    for line in data:
        fout.write(line.replace("'", "").replace("$100.00", "$75.00").replace("$25.00", "$0.00")) # Writing out + updating

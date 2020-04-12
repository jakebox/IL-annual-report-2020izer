# IL-annual-report-2020izer

In 2020 the IL Secretary of State updated their form for annual reports for corporations, so this series of scripts moves the data from 2019 documents to the new 2020 ones. Takes in 2019-style PDFS in the input_pdfs folder and runs a series of scripts (my chaining is probably silly...) and outputs them to the output_pdfs folder. Utilizes the Python library pdfminer and the utility [pdfforms](https://pypi.org/project/pdfforms/) to actually fill out the forms. It works well enough!

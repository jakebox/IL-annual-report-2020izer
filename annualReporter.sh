#!/bin/bash

start=`date +%s`

cd input_pdfs
echo "Creating CSVs"
sh csvGenerator.sh
cd ../theaction
echo "Filling out 2020 Annual Report Form"
sh pdfFiller.sh
echo "Done!"

end=`date +%s`
runtime=$((end-start))
echo Done! PDFS 2020-ized in: $runtime seconds

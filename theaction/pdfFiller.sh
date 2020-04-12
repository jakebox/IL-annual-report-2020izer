#!/bin/bash

start=`date +%s`

for file in *.csv; do
    mv "$file" battleroom/
    echo "Moved file"
    cd battleroom/
    pdfforms fill --no-flatten "$file"
    echo "Form filled"
    mv filled/blank_form.pdf ../../output_pdfs/"$file".pdf
    cd ../
done
cd battleroom/
rm *.csv
cd ../../output_pdfs

for file in *.pdf; do
    remove_spaces=`echo $file | sed -e 's/ /_/g'`
    filename_fixed_pdf=`echo $remove_spaces | sed -e 's/csv/pdf/g'`
    filename_fixed=`echo $filename_fixed_pdf | rev | cut -c 5- | rev`
    mv "$file" $filename_fixed
done

end=`date +%s`
runtime=$((end-start))
echo PDFS filled out in: $runtime seconds

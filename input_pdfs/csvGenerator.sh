#!/bin/bash
for file in *.pdf; do
    echo $file
    python3 formParser.py "$file"
done

mv *.csv ../theaction
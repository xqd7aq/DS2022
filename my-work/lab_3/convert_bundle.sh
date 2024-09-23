#!/bin/bash

#get data
curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

# Decompress
tar -xzf lab3-bundle.tar.gz

# awk can remove spaces
awk '!/^[[:space:]]*$/' lab3_data.tsv 

# convert from tsv to csv
sed 's/\t/,/g' lab3_data.tsv > lab3_data.csv

# count lines in file (old way wasn't working)
#line_count=$(wc -l lab3_data.csv)
#line_count=$(($line_count - 1))

# count lines in file
line_count=$(wc -l < lab3_data.csv)
line_count=$(($line_count - 1))
echo "The number of data lines is: $line_count"


# create a new tar file CSV file
tar -czf lab3-csv-bundle.tar.gz lab3_data.csv

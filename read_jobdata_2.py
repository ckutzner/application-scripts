#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Initialize the data dictionary
data_dictionary = {'Jobtitle:':'', 'Quelle:':'', 'Referenznummer:':'', 'Firma:':'', 'Ansprechperson:':'', 'Strasse:':'', 'PLZ:':'', 'Ort:':'', 'Telefon:':'', 'Email:':'', 'Anrede:':'', 'Jobdescription:':''}

print "\n"



# Read the jobdata file and fill the dictionary
with open("sample-data/jobdata.txt", mode='rt') as f:
    for line in f:
        tokens = line.split(None,1)
        first_token = tokens[0]
        remaining_tokens = tokens[1]

        if remaining_tokens == '':
            continue;

        if first_token not in data_dictionary.keys():
            print "WARNING: First token "+first_token+" not a key of the data_dictionary."
            continue;

        data_dictionary[first_token] = remaining_tokens
        

# Give warning if variables are missing
for k in data_dictionary.keys():
    if data_dictionary[k] == '':
        print "WARNING: Variable "+k+" is an empty string."
    else:
        print "Variable "+k+" "+data_dictionary[k]

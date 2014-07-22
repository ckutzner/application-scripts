#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Call this script from your main job application directory.

import datetime
vjob/output directory
with open ('current_jobdirectory', 'r') as d:
	jobdir = d.readline().strip()

# Initialize the data dictionary
data_dictionary = {'Jobtitle':'', 'Quelle':'', 'Referenznummer':'', 'Firma':'', 'Ansprechperson':'', 'Strasse':'', 'PLZ':'', 'Ort':'', 'Telefon':'', 'Email':'', 'Art der Bewerbung':''} 

# Read the jobdata file and fill the dictionary
with open("%s/jobdata.txt" % jobdir, mode='rt') as f:
    for line in f:
	trimmed_line = line.strip()
        tokens = trimmed_line.split(':',1)
        if len(tokens) < 2:
            continue;
        first_token = tokens[0]
        remaining_tokens = tokens[1]
        if remaining_tokens == '':
            continue;

        if first_token not in data_dictionary.keys():
            print "WARNING: First token "+first_token+" not a key of the data_dictionary."
            continue;

        data_dictionary[first_token] = remaining_tokens.strip()

#fill variables; this is somewhat unelegant, but the best solution to remove newline chars. 
jobtitle = data_dictionary['Jobtitle']
jobsrc = data_dictionary['Quelle']
rawref = data_dictionary['Referenznummer']
company = data_dictionary['Firma']
responsible = data_dictionary['Ansprechperson']
company_address = data_dictionary['Strasse']
company_zipcode = data_dictionary['PLZ']
company_city = data_dictionary['Ort']

# this is just a try at making a temporary csv. And yes, I know I should have a look at Python's CSV module, will do that some time. For now, this is a quick and dirty solution.
outlist = [rawref, company, company_address, company_zipcode, company_city, responsible, str(data_dictionary['Telefon']).strip(' \n'),str(data_dictionary['Email']).strip(' \n'), jobtitle, str(data_dictionary['Art der Bewerbung']).strip(' \n'), datetime.date.today().strftime("%d.%m.%Y")]
goneout = ('\"'+'\",\"'.join(outlist)+'\"')
outdatefile = str(datetime.date.today().strftime("%Y-%m-%d") + "_applications.csv")
with open(outdatefile, 'a') as temp_out:
	temp_out.write(goneout + '\n')

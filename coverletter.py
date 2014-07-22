#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Call this script from your main job application directory.

import datetime
from os import system
import os.path

#job/output directory
#jobdir = raw_input("Bitte gib ein, in welchem Verzeichnis die Jobdaten liegen: ").strip('/')
with open ('current_jobdirectory', 'r') as d:
	jobdir = d.readline().strip()
print "Job directory is: ", jobdir #for debugging

# Initialize the data dictionary
data_dictionary = {'Jobtitle':'', 'Quelle':'', 'Referenznummer':'', 'Firma':'', 'Ansprechperson':'', 'Strasse':'', 'PLZ':'', 'Ort':'', 'Telefon':'', 'Email':'', 'Art der Bewerbung':''} 

# Read the jobdata file and fill the dictionary
with open("%s/jobdata.txt" % jobdir, mode='rt') as f:
    for line in f:
	trimmed_line = line.strip()
#	print trimmed_line
        tokens = trimmed_line.split(':',1)
        if len(tokens) < 2:
            continue;
        first_token = tokens[0]
        remaining_tokens = tokens[1]
#	print first_token + ": " + remaining_tokens
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

# make refstring
if rawref == "" or rawref == " ":
	refstring = ""
else:
	refstring = "- Referenznummer: " + rawref

# turn name of responsible person into list, so that the last name can be used in the opening
rpname = responsible.split(' ')
addressee = rpname[-1]
 
#Anrede; case 1: sehr geehrte Frau, case2: sehr geehrter Herr, case3: sehr geehrte Damen und Herren
address = ""
ad_input = raw_input("""
Wähle die passende Anrede:
1 für 'Sehr geehrte Frau'
2 für 'Sehr geehrter Herr'
3 für 'Sehr geehrte Damen und Herren':
""")

if ad_input == "1":
	address = "Sehr geehrte Frau"
elif ad_input == "2": 
	address = "Sehr geehrter Herr"
elif ad_input == "3":
	address = "Sehr geehrte Damen und Herren"
else:
	print "Keinen gültigen Input für die Anrede gefunden, verwende 'Sehr geehrte Damen und Herren'"

opening = ""
if ad_input !="1" and ad_input!="2":
	opening = address
else:
	opening = address + " " + addressee

# get template file
with open('templatedata/anschreiben_strings.txt', 'r') as infile:
	template = infile.read()

with open('%s/anschreiben_opening.txt' % jobdir, 'w') as outfile:
	outfile.write(str(template) % (jobtitle, jobsrc, refstring, company, responsible, company_address, company_zipcode, company_city, opening))

# join opening together with other template files
system('cat templatedata/anschreiben1.tex %s/anschreiben_opening.txt templatedata/anschreiben2.tex > %s/anschreiben.tex' % (jobdir, jobdir))
system('rm %s/anschreiben_opening.txt' % jobdir)

# generate mail subject, write to a file
with open ('%s/current_mailsubject' % jobdir, 'w') as msubj:
	msubj.write(str('Ihr Stellenangebot „%s“ auf %s %s' % (jobtitle, jobsrc, refstring)))

# this is just a try at making a temporary csv. And yes, I know I should have a look at Python's CSV module, will do that some time. For now, this is a quick and dirty solution.
outheadings = ["Referenznummer", "Firma", "Straße Nr.", "PLZ", "Ort", "Ansprechperson", "Telefon", "Email", "Stellenbezeichnung", "Art der Bewerbung", "Datum", "Ergebnis"]
goneheadings = ('\"'+'\",\"'.join(outheadings)+'\"')

outlist = [rawref, company, company_address, company_zipcode, company_city, responsible, str(data_dictionary['Telefon']).strip(' \n'),str(data_dictionary['Email']).strip(' \n'), jobtitle, str(data_dictionary['Art der Bewerbung']).strip(' \n'), datetime.date.today().strftime("%d.%m.%Y")]
goneout = ('\"'+'\",\"'.join(outlist)+'\"')
outdatefile = str(datetime.date.today().strftime("%Y-%m") + "_applications.csv")

if not os.path.isfile(outdatefile): 
	with open (outdatefile, 'w') as temp_out:
		temp_out.write(goneheadings + '\n')

with open(outdatefile, 'a') as temp_out:
	temp_out.write(goneout + '\n')

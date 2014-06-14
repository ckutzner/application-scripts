#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

# Initialize the data dictionary
data_dictionary = {'Jobtitle':'', 'Quelle':'', 'Referenznummer':'', 'Firma':'', 'Ansprechperson':'', 'Strasse':'', 'PLZ':'', 'Ort':'', 'Telefon':'', 'Email':'', 'Art der Bewerbung':''} 

# Read the jobdata file and fill the dictionary
with open("sample-data/jobdata.txt", mode='rt') as f:
    for line in f:
        tokens = line.split(': ',1)
        first_token = tokens[0]
        remaining_tokens = tokens[1]

        if remaining_tokens == '':
            continue;

        if first_token not in data_dictionary.keys():
            print "WARNING: First token "+first_token+" not a key of the data_dictionary."
            continue;

        data_dictionary[first_token] = remaining_tokens

#fill variables; this is somewhat unelegant, but the best solution to remove newline chars. 
jobtitle = data_dictionary['Jobtitle'].strip('\n')
jobsrc = data_dictionary['Quelle'].strip('\n')
rawref = data_dictionary['Referenznummer'].strip('\n')
company = data_dictionary['Firma'].strip('\n')
responsible = data_dictionary['Ansprechperson'].strip('\n')
company_address = data_dictionary['Strasse'].strip('\n')
company_zipcode = data_dictionary['PLZ'].strip('\n')
company_city = data_dictionary['Ort'].strip('\n')

# print for test purposes
#print data_dictionary
#print jobtitle, jobsrc, rawref, company, responsible, company_address, company_zipcode, company_city

# make refstring
if rawref == "" or rawref == " ":
	refstring = ""
else:
	refstring = "- Referenznummer: " + rawref

# turn name of responsible person into list, so that the last name can be used in the opening
rpname = responsible.split(' ')
addressee = rpname[-1]
# print "Der Nachname der verantwortlichen Person lautet", addressee
 
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

#print 'So sieht der Briefanfang jetzt aus:\n', template % (jobtitle, jobsrc, refstring, company, responsible, company_address, company_zipcode, company_city, opening)

with open('sample-data/anschreiben_opening.txt', 'w') as outfile:
	outfile.write(str(template) % (jobtitle, jobsrc, refstring, company, responsible, company_address, company_zipcode, company_city, opening))

# this is just a try at making a temporary csv. And yes, I know I should have a look at Python's CSV module, will do that some time. For now, this is a quick and dirty solution.
outlist = [rawref, company, company_address, company_zipcode, company_city, responsible, str(data_dictionary['Telefon']).strip('\n'),str(data_dictionary['Email']).strip('\n'), jobtitle, str(data_dictionary['Art der Bewerbung']).strip('\n'), datetime.date.today().strftime("%d.%m.%Y")]
goneout = ('\"'+'\",\"'.join(outlist)+'\"')
outdatefile = str(datetime.date.today().strftime("%Y-%m-%d") + "_applications.csv")
with open(outdatefile, 'a') as temp_out:
	temp_out.write('\n' + goneout)

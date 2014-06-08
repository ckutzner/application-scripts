# -*- coding: utf-8 -*-
# prompt user for jobdescription and source, to be replaced with reading from other files later
jobtitle = raw_input('Bitte gib den Jobtitel an: ')
jobsrc = raw_input('Bitte gib eine Quelle ein: ')
refstring = '- Referenznummer:' + raw_input('Referenznummer:') # insert if function here later, just in case input is empty, to print empty string
company = raw_input('Firmenname: ')
apforename =  raw_input('Vorname der_des Ansprechpartner_in (oder Personalabteilung): ')
aplastname =raw_input('Nachname der_des Ansprechpartner_in: ')
company_address = raw_input('Straße und Hausnummer: ')
company_zipcode = raw_input('Postleitzahl: ')
company_city = raw_input('Ort: ')
 
#Anrede; case 1: sehr geehrte Frau, case2: sehr geehrter Herr, case3: sehr geehrte Damen und Herren

address = "Sehr geehrte Frau"

# get template file
with open('anschreiben_strings.txt', 'r') as infile:
template = infile.read()
print template #just for test purposes

print "This is how your subject line now looks like:\n", template % (jobtitle, jobsrc, refstring, company, apforename, aplastname, company_address, company_zipcode, company_city, address, aplastname)

with open('anschreiben_mit_strings.txt', 'w') as outfile:
outfile.write(str(template) % (jobtitle, jobsrc, refstring, company, apforename, aplastname, company_address, company_zipcode, company_city, address, aplastname))

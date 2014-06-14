# -*- coding: utf-8 -*-
# prompt user for jobdescription and source, to be replaced with reading from other files later
jobtitle = raw_input("Bitte gib den Jobtitel an: ")
jobsrc = raw_input("Bitte gib eine Quelle ein: ")
rawref = raw_input("Referenznummer: ") 
company = raw_input("Firmenname: ")
responsible =  raw_input("Ansprechpartner_in: ")
company_address = raw_input("Straße und Hausnummer: ")
company_zipcode = raw_input("Postleitzahl: ")
company_city = raw_input("Ort: ")

# make refstring
if rawref == "" or rawref == " ":
	refstring = ""
else:
	refstring = "- Referenznummer: " + rawref

# turn name of responsible person into list, so that the last name can be used in the opening
rpname = responsible.split(' ')
addressee = rpname[-1]
print "Der Nachname der verantwortlichen Person lautet", addressee
 
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

with open('sample-data/anschreiben_mit_strings.txt', 'w') as outfile:
	outfile.write(str(template) % (jobtitle, jobsrc, refstring, company, responsible, company_address, company_zipcode, company_city, opening))

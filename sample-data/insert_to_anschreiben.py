# prompt user for jobdescription and source, to be replaced with reading from other files later
jobtitle = raw_input('Bitte gib den Jobtitel an: ')
jobsrc = raw_input('Bitte gib eine Quelle ein: ')
refstring = raw_input('Referenznummer:')
company = raw_input('Firmenname: ')
apforename =  raw_input('Vorname der_des Ansprechpartner_in (oder „Personalabteilung“): ')
aplastname =raw_input('Nachname der_des Ansprechpartner_in: ')
company_address = raw_input('Straße und Hausnummer: ')
company_zipcode = raw_input('Postleitzahl: ')
company_city = raw_input('Ort: ')
 
#Anrede; case 1: sehr geehrte Frau, case2: sehr geehrter Herr, case3: sehr geehrte Damen und Herren

address = xyz

# get template file
infile = open('anschreiben_strings.txt', 'r')
template = infile.read()

print "This is how your subject line now looks like:\n", template % (jobtitle, jobsrc)

outfile = open('anschreiben_mit_strings.txt', 'w')
outfile.write(str(template) % (jobtitle, jobsrc))

outfile.close()
infile.close()



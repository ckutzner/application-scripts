# prompt user for jobdescription and source, to be replaced with reading from other files later
jobtitle = raw_input('Bitte gib den Jobtitel an: ')
jobsrc = raw_input('Bitte gib eine Quelle ein: ')
company = raw_input('Bitte gib den Firmennamen ein: ')
apforename =  raw_input('Bitte gib eine Quelle ein: ')
aplastname =raw_input('Bitte gib eine Quelle ein: ')
company_address = raw_input('Bitte gib eine Quelle ein: ')
company_zipcode = raw_input('Bitte gib eine Quelle ein: ')
company_city = raw_input('Bitte gib eine Quelle ein: ')
 

#Anrede; case 1: sehr geehrte Frau, case2: sehr geehrter Herr, case3: sehr geehrte Damen und Herren

# get template file
infile = open('anschreiben_strings.txt', 'r')
template = infile.read()

print "This is how your subject line now looks like:\n", template % (jobtitle, jobsrc)

outfile = open('anschreiben_mit_strings.txt', 'w')
outfile.write(str(template) % (jobtitle, jobsrc))

outfile.close()
infile.close()



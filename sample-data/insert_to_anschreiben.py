# prompt user for jobdescription and source, to be replaced with reading from other files later
jobtitle = raw_input('Bitte gib den Jobtitel an: ')
jobsrc = raw_input('Bitte gib eine Quelle ein: ')

# get template file
infile = open('anschreiben_strings.txt', 'r')
template = infile.read()

print "This is how your subject line now looks like:\n", template % (jobtitle, jobsrc)

outfile = open('anschreiben_mit_strings.txt', 'w')
outfile.write(str(template) % (jobtitle, jobsrc))

outfile.close()
infile.close()



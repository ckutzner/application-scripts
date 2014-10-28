#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Call this script from your main job application directory; enter start date and stop date (format m or mm, eg. 7 for July and 11 for November) as command line arguments 

import sys
import datetime
import os
import fnmatch
#import codecs
import csv

# enter start and stop month
start = int(sys.argv[1]) # start month
stop = int(sys.argv[2]) # stop month

# make loopable range from months
if stop <= start:
	stop += 12
months = range(start, stop+1)

filelist = []

# generate raw filelist
raw_filelist = fnmatch.filter(os.listdir('.'), '[0-9][0-9][0-9][0-9]-[0-1][0-9]*[a-z].csv')

# filter raw filelist for occurrence of months
for i in months:
	if i > 12:
		i -= 12
	for a in fnmatch.filter(raw_filelist, '[0-9][0-9][0-9][0-9]-*%d*.csv' % i):
		filelist.append(a)
	
#read from filelist
for f in filelist:
	with open(f, 'r') as g:
		reader = csv.DictReader(g, delimiter=",")	 	# build list of dictionaries
		for row in reader:					# loop through list
			if row['Ergebnis'] == "" or row['Ergebnis'] == None:
				row['Ergebnis'] = " " 
			if row['Telefon'] == "" or row['Telefon'] == " " or row['Telefon'] == None:
				contact = row['Email']
			else:
				contact = str(row['Telefon']+'\\newline '+row['Email'])
			out_line= [row['Datum'], str(row['Firma'].replace('&','\\&') + "\\newline " + row['Straße Nr.'] + "\\newline " + row['PLZ'] + " " + row['Ort']), contact, row['Ansprechperson'], row['Stellenbezeichnung'].replace('&','\\&'), row['Art der Bewerbung'], row['Ergebnis']]
#			print out_line
			outline = str(' & '.join(out_line))
			h = open('report_lines.tex', 'a+')			# write to the outfile
			h.write(outline + '\\\ \hline\n')	 	# write to outfile
			h.close()					# then close the file

output_filename = 'report_' + str(datetime.date.today().strftime("%Y-%m-%d") + '.tex' # possibly reverse this, or integrate if/else switch
output_file = open(output_filename,'w')
output_file.write('\\input{report-header.tex}')
output_file.write('\\begin{center}
\\begin{tabular}{|p{21mm}|p{45mm}|p{40mm}|p{30mm}|p{45mm}|p{20mm}|p{38mm}|} \hline % alignment of table columns
\\input{reportheadings.tex} ') # make a file of its own of this one

# WHILE LOOP über die zeilen in report-lines.tex
with open('report_lines.tex', 'r') as f:
	for line in f: 
				
# beijeder Iteration checke, ob man die max Anzahl der Zeilen erreicht hat
# wenn ja, starte eine neue Tabelle
# ganz am ende füge \end tabular, \end center und \end document hinzu

output_file.close()
# bonus points for function that only produces entries in a given timedelta (e.g. from 2014-07-23 to 2014-10-22) instead of months

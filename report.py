#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Call this script from your main job application directory; enter start date and stop date (format m or mm, eg. 7 for July and 11 for November) as command line arguments 

import sys
import datetime
import os
import fnmatch
import codecs

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
	
# read from final files; certainly there is a more elegant way using the csv class and unicode, like described below there: https://docs.python.org/2/library/csv.html#examples . For now, I'll stick with this clumsy workaround.
for f in filelist:
	g = codecs.open(f, encoding='utf-8') #needed bccsv files contain unicode characters
	for line in g:
		sline= line.strip('\n"') # remove newline characters and quotes at the beginning of lines
		line_list = sline.split('","') # make list, separated by commas surrounded by quotes
		outline = ' & '.join(line_list) # join list back by LaTeX field separators
		h = codecs.open('report_test.tex', encoding='utf-8', mode='a+')  # then write it to the outfile 
		h.write(outline + '\\\ \hline\n')
		h.close() # Finally, close the files 
	g.close()
# what to do: 
# rewrite: assign to variables?
# rearrange and join fields according to jobcenter requirements
# learn how to do fields with line wraps in LaTeX tables, either write formatting for it or incorporate it in writing program
# bonus points for function that only produces entries in a given timedelta (e.g. from 2014-07-23 to 2014-10-22) instead of months

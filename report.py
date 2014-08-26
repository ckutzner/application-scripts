#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Call this script from your main job application directory; enter start date and stop date as command line arguments 

import sys
import datetime
import os
import fnmatch

# enter start and stop month
start = int(sys.argv[1]) # start month
stop = int(sys.argv[2]) # stop month

# make loopable range from months
if stop <= start:
	stop += 12
months = range(start, stop+1)
print months #for test purpose

filelist = []

# generate raw filelist
raw_filelist = fnmatch.filter(os.listdir('.'), '[0-9][0-9][0-9][0-9]-[0-1][0-9]*[a-z].csv')
print raw_filelist #for test purpose

# filter raw filelist for occurrence of months
for i in months:
	if i > 12:
		i -= 12
	for a in fnmatch.filter(raw_filelist, '[0-9][0-9][0-9][0-9]-*%d*.csv' % i):
		filelist.append(a)
	
print '\n'.join(filelist) # for test purposes	

# read from final files
#for f in filelist:
#	with open(file, 'r') as d: 
	

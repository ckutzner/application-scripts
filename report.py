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
if stop >= start:
	stop += 12
months = range(start, stop+1)

filelist = []
files_in_dir = os.listdir('.')

for i in months:
	if i > 12:
		i -= 12
		

# determine file
for f in filelist:
	with open(file, 'r') as d: 
	

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Call this script from your main job application directory

import datetime
from os import system

# enter start and stop date
start_date = raw_input("Bitte gib den Startmonat des Berichts im Format 'mm' ein: ")
stop_date = raw_input("Bitte gib den Endmonat des Berichts im Format 'mm' ein: ")

# read from csv
with open(datafile, 'r') as d:
	

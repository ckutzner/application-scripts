#!/bin/bash
# Skript, das nicht mehr benötigte Files löscht; call from main directory. Achtung: danach können alle Bewerbungsskripte, die auf current_jobname und current_directory zugegriffen haben, nicht mehr ausgeführt werden!

if [ -f current_jobdirectory ]
then
	jobdir=$(head -1 current_jobdirectory)
#	echo $jobdir # for test purposes
	rm ${jobdir}/*.aux 2> /dev/null
	rm ${jobdir}/*.bak 2> /dev/null
	rm ${jobdir}/*.log 2> /dev/null
	rm ${jobdir}/*.out 2> /dev/null
	rm ${jobdir}/*.swp 2> /dev/null
	rm ${jobdir}/*.*~ 2> /dev/null
	rm current_*
else 
	echo "current_jobdirectory not found, all finished."
fi

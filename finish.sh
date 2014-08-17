#!/bin/bash
# Skript, das nicht mehr benötigte Files löscht; call from main directory. Achtung: danach können alle Bewerbungsskripte, die auf current_jobname und current_directory zugegriffen haben, nicht mehr ausgeführt werden!

jobdir=$(head -1 current_jobdirectory)
echo $jobdir
rm ${jobdir}/*.aux
rm ${jobdir}/*.bak
rm ${jobdir}/*.log
rm ${jobdir}/*.out
rm ${jobdir}/*.swp
rm ${jobdir}/*.*~

rm current_*

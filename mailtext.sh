#!/bin/bash
# This script generates mail.txt which, in turn, becomes the body text for the mail. Planned feature: strip unnecessary lines from text files, keep only opening of body of cover letter, but maybe add salutation (this could also be handled by mail-composition script).

sed 's/nummer(.*)\\,/nummer\s/g' anschreiben.tex > temp1.tex
sed 's/nummer(\s.*)~/nummer\1\s/g' temp1.tex > temp2.tex
awkwhere=$(echo $(which mailtext.sh) | sed 's/mailtext.sh$//')
echo $awkwhere #for test purposes

if [ -z "$awkwhere" ]
	then echo "error, part of the mailtextedit program could not be found. please check your PATH variable!"
fi 

detex temp2.tex | awk -f $awkwhere/mailtextedit.awk > mail.txt
rm temp1.tex temp2.tex

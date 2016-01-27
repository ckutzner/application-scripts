#!/bin/bash
# This script generates mail.txt which, in turn, becomes the body text for the mail. Planned feature: strip unnecessary lines from text files, keep only opening of body of cover letter, but maybe add salutation (this could also be handled by mail-composition script).

# check if anschreiben.tex exists
if [ ! -f anschreiben.tex ]
	then echo "error, anschreiben.tex does not exist! Please edit your cover letter first." >&2
	exit 1
fi

sed 's/nummer(.*)\\,/nummer\s/g' anschreiben.tex > temp1.tex
sed -r 's/nummer(\s.*)~/nummer\1\s/g' temp1.tex > temp2.tex
awkwhere=$(echo $(which mailtext.sh) | sed 's/mailtext.sh$//')

# error message if awk script can't be found
if [ -z $awkwhere ]
	then echo "error, part of the mailtextedit program could not be found. please check your PATH variable!" >&2
	exit 1
fi 
echo $awkwhere #for test purposes

detex temp2.tex | awk -f $awkwhere/mailtextedit.awk > mail1.txt
rm temp1.tex temp2.tex

# füge nach der Grußformel eine Leerzeile ein
sed -i '1a\\' mail1.txt
cat -s mail1.txt > mail.txt 
rm mail1.txt

exit 0

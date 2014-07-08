#!/bin/bash
# This script generates mail.txt which, in turn, becomes the body text for the mail. Planned feature: strip unnecessary lines from text files, keep only opening of body of cover letter, but maybe add salutation (this could also be handled by mail-composition script).

awkwhere=$(echo $(which mailtext.sh) | sed 's/mailtext.sh$//')
detex anschreiben.tex | awk -f $awkwhere/mailtextedit.awk > mail.txt




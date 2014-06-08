quelle = ''
jobtitle = ''


with open("jobdata.txt", 'rt') as f:
    for line in f:
        tokens = line.split(None,1)
        first_token = tokens[0]
        remaining_tokens = tokens[1]
        print tokens
        print first_token
        print remaining_tokens

        if firsttoken == 'Quelle':
            quelle = first_token
        elif first_token == 'Jobtitle':
            jobtitle = first_token
        else:
            print "ERROR: First token "+first_token+" not recognized."
        

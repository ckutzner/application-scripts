BEGIN {found_start = 0;}

($1 == "Sehr") {found_start = 1;}

(found_start == 1) {print $0;}

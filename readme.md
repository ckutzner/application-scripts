# A bash + pyhton toolset for job applications
Just some bash and Python scripts that help me apply for jobs faster and better by doing the tedious no-brainer work for me.

My application process relies heavily on LaTeX and the bash. Further utilities used are aspell for spell checking and thunderbird for sending mail.

This toolset is developed and tested under Ubuntu 12.04, Ubuntu 14.04 and ArchLinux. Tests with other Linux/Unix-based systems are appreciated. Ports to other OS are welcome, too.

You will find a sample project in the folder sample-data. Use this if you don't want to test the utilites on "live" data.

The (optional) report feature is used for generating reports for the German Jobcenters. 

## Requirements
This toolset uses:

* bash
* so far, Python 2, but I plan to switch to Python 3 with any future modifications.
* LaTex/pdflatex and detex
* sed and awk
* pdfjoin/pdfjam

## Known limitations
Because this is a "scratch my own itch" project, I wrote it around my own application process. That means: 

* LaTeX-centric.
* So far, the documents used in this toolset conform to German standards (re: letter class, addresses, etc.). Input for other countries is welcome.
* Uses Thunderbird as email client for sending out applications.
* **One application at a time.** For me, this is an anti-procrastination, anti-getting bogged down feature/useful constriction.
* so far, Linux/Unix-only. But if you want to make a version for Windows or other OS, go ahead and fork me!
* I don't plan to make a GUI, b/c I tend to find GUIs distracting, and making one doesn't pertain to "scratching my own itch". If you want to make one: fork me!

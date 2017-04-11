Run Instructions for extweetwordcount

Note: Please run everything from the extweetwordcount folder as the w205 user in the ami-d4dd4ec3 (UCB MIDS W205 EX2-FULL) instance on AWS.  All dependencies specified in the Architecture file must be preinstalled.

File Setup
Please make sure Postgres is running.
The first step after received extweetcount is to run prerun.py.  This will remove any data you may have already stored in tcount and create a new clean copy of tcount.  In addition, it will add the credentials you specified in this script in so that the data stream will work. Additional info on this script can be found by using '-h' in the python command.


[w205@ip-172-31-73-176 extweetwordcount]$ python prerun.py -h

This scripts helps set up the Postgres database you will need
prior to running the twitter stream.  It will also load in all API
information needed required to connect to twitter.

    -c Consumer Key (create via apps.twitter.com)
    -s Consumer Secret (create via apps.twitter.com)
    -k Access Key (create via apps.twitter.com)
    -a Access Secret (create via apps.twitter.com)
    -h help menu


Stream Twitter
Simply run 'sparse run'.  Once you have enough data, please press ctrl-C to stop the stream.  All the tweeted words from starting the stream up to when you press ctrl-c will be stored in the tcount database.

Post Processing
To view the data, finalresults.py or histogram.py are available to run.  Both have a help menu available for the options if you input '-h' into the python command.

[w205@ip-172-31-73-176 extweetwordcount]$ python finalresults.py -h

When passed a word (w), script will return the total number of word
occurrences in the stream. If no word is specified, it will returns all
words in the stream, and their total count of occurrences, sorted
alphabetically. Script will also generate plot.txt of the top 20 words
which can be used to create a bar graph or any other needed figure.

    -w word to display count for
    -h this help menu

[w205@ip-172-31-73-176 extweetwordcount]$ python histogram.py -h

The script gets two integers (a,b) and returns all the words with a
total number of occurrences greater than or equal to a, and less than
or equal to b.

    -a min count to display
    -b max count to display
    -h this help menu


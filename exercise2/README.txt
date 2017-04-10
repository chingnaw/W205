extweetcount Instructions.

Please run everything from the extweetcount folder.  All dependencies specified in the Architecture folder must be preinstalled.

The first step after received extweetcount is to run prerun.py.  This will remove any data you may have already stored in tcount and create a new clean copy of tcount.

The next step is to enter the credentials from your Twitter API.  Please refer to the Architecture file if your API is not set up properly.  The information must be entered into the /src/tweets.py script where noted.

After setting up the Postgres database, you can run 'sparse run'.  Once you have collected all the data you want, please press ctrl-C to stop the stream.  All the tweeted words from starting the stream will be stored in the tcount database.  

Now you can run either finalresults.py or histogram.py.  Both have a help menu available for the options if you input '-h' into the python command.


[w205@ip-172-31-73-176 extweetwordcount]$ python finalresults.py -h

When passed a word (w), script will return the total number of
word occurrences in the stream. If no word is specified, it will returns all words
in the stream, and their total count of occurrences, sorted alphabetically.
Script will also generate plot.png which will display the top 20 words in a bar graph.

    -w word to display count for
    -h this help menu



[w205@ip-172-31-73-176 extweetwordcount]$ python histogram.py -h

The script gets two integers (a,b) and returns all the words with
a total number of occurrences greater than or equal to a, and less than or equal to b.

    -a min count to display
    -b max count to display
    -h this help menu


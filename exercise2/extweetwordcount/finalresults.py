from getopt import getopt
import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from operator import itemgetter



HELP_STRING = """When passed a word (w), script will return the total number of 
word occurrences in the stream. If no word is specified, it will returns all words 
in the stream, and their total count of occurrences, sorted alphabetically.
Script will also generate plot.png which will display the top 20 words in a bar graph.

    -w word to display count for
    -h this help menu

"""

# DEFAULTS 
word = None

# retrieve the user parameters

try:
    optlist, args = getopt(sys.argv[1:], "hw:")
except:
    print "Error retrieving options"
    print ""
    print HELP_STRING
    sys.exit(1)

for (opt, opt_arg) in optlist:
    if opt == "-h":
        print ""
        print HELP_STRING
        sys.exit(1)
    elif opt == "-w":
        word = str(opt_arg)

# check required parameters exist, and exit otherwise
#if():
#    print HELP_STRING
#   sys.exit(1)


# do the actual work
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")


if word:
    #some code that will search database for that word, print that record
    #print word
    cur = conn.cursor()
    cur.execute("SELECT word, count from tweetwordcount WHERE word = %s", (word,))
    records = cur.fetchall()
    if len(records) == 0:
        print "%s did not appear in the twitter stream." % word
    else:
        for rec in records:
            print "Total number of occurrencies of %s: %s" % (rec[0],rec[1])
    conn.commit()

elif word == None:

    cur = conn.cursor()
    cur.execute("SELECT word, count from tweetwordcount")
    records = cur.fetchall()
    records_alphabetical = sorted(records,key=itemgetter(0))
    for rec in records_alphabetical:
       print "%s: %s" % (rec[0],rec[1])
    conn.commit()

out = open('plot.txt','w')

cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount")
records = cur.fetchall()
records_sorted = sorted(records,key=itemgetter(1), reverse=True)
conn.commit()

for rec in records_sorted[:20]:
    out.write("%s\t%s\n" % (rec[0],rec[1]))

out.close()

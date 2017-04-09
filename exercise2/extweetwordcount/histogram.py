from getopt import getopt
import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


HELP_STRING = """The script gets two integers (a,b) and returns all the words with 
a total number of occurrences greater than or equal to a, and less than or equal to b.

    -a min count to display
    -b max count to display
    -h this help menu

"""

# DEFAULTS 
min = 0
max = 0

# retrieve the user parameters

try:
    optlist, args = getopt(sys.argv[1:], "ha:b:")
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
    elif opt == "w":
        word = opt_arg

# check required parameters exist, and exit otherwise
if(min == max):
    print "Please set different values for the minimum and maximum values"
    print HELP_STRING
    sys.exit(1)


# do the actual work
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")


cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount WHERE count between %s and %s", (min,max))
records = cur.fetchall()
records_sorted = sorted(records,key=itemgetter(1))
for rec in records_sorted:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

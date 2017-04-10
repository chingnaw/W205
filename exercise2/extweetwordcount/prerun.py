from getopt import getopt
import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



HELP_STRING = """Description of script
    -c Consumer Key
    -s Consumer Secret
    -k Access Key
    -a Access Secret
    -h help menu
"""
#Defaults
consumer_key = None
consumer_secret = None
access_key = None
access_secret = None

# retrieve the user parameters
try:
    optlist, args = getopt(sys.argv[1:], "hc:s:k:a:")
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
    elif opt == "-c":
        consumer_key = str(opt_arg)
    elif opt == "-s":
        consumer_secret = str(opt_arg)
    elif opt == "-k":
        access_key = str(opt_arg)
    elif opt == "-a":
        access_secret = str(opt_arg)

# check required parameters exist, and exit otherwise
if():
   print HELP_STRING
  sys.exit(1)

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

try:
    # CREATE DATABASE can't run inside a transaction
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.close()
except:
    print "Could not create tcount"

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()



##add the correct API keys into the tweet spout code
os.system("sed -i 's/CONSUMERKEY/%s' ./src/spouts/tweets.py" % consumer_key)
os.system("sed -i 's/CONSUMERSECRET/%s' ./src/spouts/tweets.py" % consumer_secret)
os.system("sed -i 's/ACCESSKEY/%s' ./src/spouts/tweets.py" % access_key)
os.system("sed -i 's/ACCESSSECRET/%s' ./src/spouts/tweets.py" % access_secret)


# This script reads a standard Excel CSV where some values have 
# multiple lines and replaces each embedded newline with the 
# \n sequence. This prepares the file for import into assembla.

import sys
import csv

w = csv.writer(sys.stdout)
for line in csv.reader(open(sys.argv[1])):
    for i in xrange(len(line)):
        line[i] = line[i].replace('\n', '\\n')
    w.writerow(line)
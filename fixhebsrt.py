import sys
import pysrt
from bidi.algorithm import get_display

print sys.argv[1]
subs = pysrt.open(sys.argv[1], encoding='utf8')

print len(subs)
for sub in subs:
    print sub.text
#CAUTION: DELETES FILES!!
COMMENT THIS TO CONFIRM INTENTION

import os
import sys

try:
    fileobj = open(sys.argv[1], 'r')
except IndexError:
    fileobj = sys.stdin

with fileobj:
    data = fileobj.read()

files = data.split('\n')

deleted_files_count = 0
for root, directories, filenames in os.walk('/home/shamanyu/Pictures/Pics'):
    for filename in filenames:
        filename = '/home/shamanyu/Pictures/Pics/'+filename
        if filename in files:
            os.remove(os.path.join('/home/shamanyu/codes/Pictures/Pics', filename))
            deleted_files_count = deleted_files_count + 1

print "You have deleted ", deleted_files_count, "files"


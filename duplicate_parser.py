import sys
try:
    fileobj = open(sys.argv[1], 'r')
except IndexError:
    fileobj = sys.stdin

with fileobj:
    data = fileobj.read()
    lines = data.split('\n')
    for line in lines:
        file_to_remove = line.split(' ')[4]
        print file_to_remove

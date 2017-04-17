#CAUTION: DON'T RUN MORE THAN ONCE!!
COMMENT THIS TO CONFIRM INTENTION

import os

files = list()

id = 0

for root, directories, filenames in os.walk('/home/shamanyu/Pictures'):
    for filename in filenames: 
        id = id + 1
        new_name = "image2015_"+str(id)
        filename_split = filename.split(".")
        new_filename = filename_split[1:]
        new_filename.insert(0, new_name)
        new_filename = '.'.join(new_filename)
        os.rename(os.path.join(root, filename), os.path.join('/home/shamanyu/Pictures/', new_filename))

print "You have got ", id, "files"

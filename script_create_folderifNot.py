import sys, os
from os import listdir
from os.path import isfile, join, isdir

mypath = sys.path[0]

if not isdir(join(mypath, 'test_folder')):
    !mkdir test_folder 
    directory = join(mypath, 'test_folder')
    os.chdir(directory)
    with open('test.txt','w') as f:
        f.write('test')
    os.chdir(mypath)
else:
    directory = join(mypath, 'test_folder')
    os.chdir(directory)
    with open('second_file.txt','w') as f:
        f.write('second')
    os.chdir(mypath)
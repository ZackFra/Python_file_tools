import os
import glob
import filecmp
from gather_r import gather_r

def rmdup_r(path):
    if os.path.exists(path):
        if path[-1] == '/':
            path = path + '*'
        else:
            path = path + '/*'
        rmdup_r_util(path, [])
        
    else:
        print("{} does not exist".format(path))
        return -1

def rmdup_r_util(path, files):
    files.extend(glob.glob(path))
    dirs = []
        
    # remove all directories from files
    # and store them in the dirs list
    for potentialDir in files:
        if os.path.isdir(potentialDir):
            dirs.append(potentialDir)

    for dir in dirs:
        files.remove(dir)

    for f in files:
        for potentialDup in files:    
            if f != potentialDup:
                if os.path.exists(potentialDup) and os.path.exists(f):
                    if filecmp.cmp(f, potentialDup):
                        os.remove(potentialDup)

    # remove the deleted directories from the list of files
    for f in files:
        if not os.path.exists(f):
            files.remove(f)
        
    for dir in dirs:
        rmdup_r_util(dir + '/*', files)

if __name__ == '__main__':
    # flow of execution begins here
    path = input("Enter the folder with duplicates: ")
    if rmdup_r(path) != -1:
        choice = input("Shall I gather the remaining files into the top directory?: ")
        if choice == 'y':
            gather_r(path, '*', path)



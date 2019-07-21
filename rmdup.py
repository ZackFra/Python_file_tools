import os
import glob
import filecmp

def rmdup(path):
    if os.path.exists(path):
        if path[-1] == '/':
            path = path + '*'
        else:
            path = path + '/*'

        files = glob.glob(path)
        for f in files:
            for potentialDup in files:
                
                if f != potentialDup:
                    if os.path.exists(potentialDup) and os.path.exists(f):
                        if filecmp.cmp(f, potentialDup):
                            os.remove(potentialDup)

# flow of execution begins here
if __name__ == '__main__':
    path = input("Enter the folder with duplicates: ")
    rmdup(path)



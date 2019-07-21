import os
import shutil
import glob
from rename import get_new_name

GATHER_PATH = './gathered'

# cleans up the input, checks if input valid prior to extracting
def gather(path, ext, target=GATHER_PATH):

   ext = ext.strip()
   path = path.strip()
   
   if ext[0] != '.' and ext != '*':
      ext = '.' + ext

   # if the path specified exists, gather
   if os.path.isdir(path):
      if not os.path.isdir(target):
         os.mkdir(target)
      gather_util(path, ext, target)
      if os.path.exists('./tmp'):
         os.remove('./tmp')
   # if path doesn't exist, print error message
   else:
      print("{} does not exist.".format(path))
   
# recursivly extract files from a given folder
# and extract files from any subfolders that
# have the extention ext
def gather_util(path, ext, target):
   
   query = path + '/*' + ext

   # for file in glob.glob(query),
   # check if it is in target already
   # if it isn't copy it into target
   files = glob.glob(query)
   for f in files:
      if os.path.dirname(f) != target and not os.path.isdir(f):

         file_name = f.split('/')[-1]

         # if two files have the same name, rename the duplicate
         if os.path.exists(target + '/' + file_name):
            new_file_name = get_new_name(target + '/' + file_name)
            os.rename(f, new_file_name)
            
         # otherwise just move it as is
         else:
            shutil.move(f, target)

if __name__ == '__main__':
   # Flow of execution starts here
   ext = input("Enter the extensions you want to find: ")
   path = input("Enter the directory to search: ")
   dest = input("Enter the destination (ignore for ./gathered): ")
   if(dest == ''):
      gather(path, ext)
   else:
      gather(path, ext, dest)

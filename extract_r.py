import os
import shutil
import glob
from rename import get_new_name

EXTRACT_PATH = './extracted'

   
# cleans up the input, checks if input valid prior to extracting
def extract_r(path, ext, target=EXTRACT_PATH):

   ext = ext.strip()
   path = path.strip()
   
   if ext[0] != '.' and ext != '*':
      ext = '.' + ext

   # if the path specified exists, extract
   if os.path.isdir(path):
      if not os.path.isdir(target):
         os.mkdir(target)
      extract_r_util(path, ext, target)

      # if a temp file was made, delete it
      if os.path.exists('./tmp'):
         os.rmdir('./tmp')
         
   # if path doesn't exist, print error message
   else:
      print("{} does not exist.".format(path))
   
# recursivly extract files from a given folder
# and extract files from any subfolders that
# have the extention ext
def extract_r_util(path, ext, target):
   
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
            if not os.path.exists('./tmp'):
               os.mkdir('./tmp')

            temp_path = './tmp/' + f.split('/')[-1]
            new_file_name = get_new_name(target + '/' + file_name)
            
            shutil.copy(f, './tmp')
            os.rename(temp_path, new_file_name)
            
         # otherwise just copy it as is
         else:
            shutil.copy(f, target)

   # get a list of all directories in the current path
   # for each potential path, check that it is a directory
   # if it is, extract any files from that path with the
   # ext extension
   paths = os.listdir(path)
   for p in paths:
      if os.path.isdir(path + '/' + p):
         extract_r_util(path + '/' + p, ext, target)

if __name__ == '__main__':
   # Flow of execution starts here
   ext = input("Enter the extensions you want to find: ")
   path = input("Enter the directory to search: ")

   extract_r(path, ext)

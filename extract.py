import os
import shutil
import glob
from rename import get_new_name

EXTRACT_PATH = './extracted'
   
# cleans up the input, checks if input valid prior to extracting
def extract(path, ext, target=EXTRACT_PATH):

   ext = ext.strip()
   path = path.strip()
   
   if ext[0] != '.' and ext != '*':
      ext = '.' + ext

   # if the path specified exists, extract
   if os.path.isdir(path):
      if not os.path.isdir(target):
         os.mkdir(target)
      extract_util(path, ext, target)

      # if a temp file was made, delete it
      if os.path.exists('./tmp'):
         os.rmdir('./tmp')
         
   # if path doesn't exist, print error message
   else:
      print("{} does not exist.".format(path))
   
# extract files from a given folder
def extract_util(path, ext, target):
   
   query = path + '/*' + ext

   # remove all directories from files
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

if __name__ == '__main__':
   # Flow of execution starts here
   ext = input("Enter the extensions you want to find: ")
   path = input("Enter the directory to search: ")
   target = input("Enter directory you want thise files extracted to (ignore for ./extracted): ")

   target = target.strip()
   if target == '':
      extract(path, ext)
   else:
      extract(path, ext, target)

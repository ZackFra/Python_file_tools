import os

def get_new_name(file_path):
   fp = file_path.split('.')
   i = 0
   while os.path.exists(file_path):
      file_path = '.' + fp[0] + fp[1] +'(' + str(i) + ').' + fp[2]
      i += 1
      
   return file_path

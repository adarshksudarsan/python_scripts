"""
#######################################################
script to search files in your directory(ver 1)
#######################################################
"""

import os
import fnmatch
import sys

def find(search, path):
  result=[]
  for root, dirs, files in os.walk(path):
    for name in files:
      if fnmatch.fnmatch(name,search):
        result.append(os.path.join(root, name)) 
  return result
"""
here i have used "*" in print statement ,it is a way of displaying list in python
and to view in seperate lines i have used "sep="\n""
""" 
print(*find('*'+sys.argv[1],sys.argv[2]),sep="\n")
#modificationbutnomodification


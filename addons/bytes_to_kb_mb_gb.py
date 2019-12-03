
# coding: utf-8

# In[ ]:


import os
import math
size_bytes= os.path.getsize('/home/vvdn/Desktop/final2.csv')
print(size_bytes)
def convert_size(size_bytes): 
    if size_bytes == 0: 
        return "0B" 
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB") 
    i = int(math.floor(math.log(size_bytes, 1000)))
    power = math.pow(1000, i) 
    size = round(size_bytes / power, 2) 
    return "{} {}".format(size, size_name[i])
print(convert_size(size_bytes))


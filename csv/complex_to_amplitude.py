'''
applymap() is a function in pandas here x corresponds to each element in the dataframe
'''

import pandas as pd
import numpy as np

frame1=pd.read_csv("/home/vkchlt0300/Music/new.csv")

def every(x):
    x=complex(x)
    return abs(x)


frame1=frame1.applymap(every)
print(frame1)
#csv 
frame1.to_csv('/home/vkchlt0300/Desktop/final_siva.csv',index=False,header=False)
print("all_done_bro")

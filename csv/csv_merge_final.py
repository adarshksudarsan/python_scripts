
# coding: utf-8

# In[ ]:


import pandas as pd
import glob

#give the path of csv files(with object)
path1 = r'/home/vvdn/ML/job_jishnu/test/dataset/object_amplitude'
all_files1 = glob.glob(path1 + "/*.csv")

for f1 in all_files1:
    frame1=pd.concat((pd.read_csv(f1,delimiter='\t') for f1 in all_files1))
frame1.drop(frame1.columns[len(frame1.columns)-2], axis=1, inplace=True)
frame1.drop(frame1.columns[len(frame1.columns)-1], axis=1, inplace=True)
frame1['head'] =1


#path to csv files(with no objects)
path2 = r'/home/vvdn/ML/job_jishnu/test/dataset/No_object_amplitude/'
all_files2 = glob.glob(path2 + "/*.csv")

for f2 in all_files2:
    frame2=pd.concat((pd.read_csv(f2,delimiter='\t') for f2 in all_files2))
frame2.drop(frame2.columns[len(frame2.columns)-2], axis=1, inplace=True)
frame2.drop(frame2.columns[len(frame2.columns)-1], axis=1, inplace=True)
frame2['head'] =0

#csv merging
bigdata = frame1.append(frame2, ignore_index=True)
# give path for final output
bigdata.to_csv('/home/vvdn/Desktop/final.csv')


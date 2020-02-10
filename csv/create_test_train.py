#give the desired shape in iloc

import pandas as pd
#reading
df1=pd.read_csv('human_ch0_complex.csv',header=None)

#reshaping to desired size 
df1=df1.iloc[0:3000,0:52]
'''
#to find amplitude
def every(x):
    try:
        x=complex(x)
        return(int(abs(x)))
    except:
        print("fine")
        return(x)

df1=df1.applymap(every)
'''
#testing_data
test_data=df1.iloc[2901:3000,0:52]

#training data
df=df1.iloc[0:2900, 0:52]
df[52]=0
#saving testing and training data csv
df.to_csv('train.csv',header=None,index=None)
test_data.to_csv('test.csv',header=None,index=None)

print("done")

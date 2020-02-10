import pandas as pd
df1=pd.read_csv('cmplx_data/human_ch0.csv',header=None)
df2=pd.read_csv('cmplx_data/human_ch1.csv',header=None)
df3=pd.read_csv('cmplx_data/noobj_ch0.csv',header=None)
df4=pd.read_csv('cmplx_data/noobj_ch1.csv',header=None)

frames = [df1, df2, df3,df4]
result = pd.concat(frames)
result.to_csv('merged.csv',header=None,index=None)
print("done")

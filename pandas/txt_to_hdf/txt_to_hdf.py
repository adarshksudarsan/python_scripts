import glob
import pandas as pd
read_files = glob.glob("0/*.txt")

with open("resultfinal.txt", "a") as outfile:
    for f in read_files:
        print(f)
        with open(f, "r") as infile:
            for lne in infile:
                print (lne)
                outfile.write(lne +"\n")
df = pd.read_table("resultfinal.txt",delimiter=",",header=None)
df.to_hdf('DATA.h5', key='df', mode='w')
print("**DONE**")

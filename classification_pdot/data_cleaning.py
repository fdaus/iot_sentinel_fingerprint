
import pandas as pd


df = pd.read_csv("csv_full_fingerprint/Aria/file_Aria_1.csv")

print (df.shape)
# select 12 unique vector fingerprints

df = df.drop_duplicates()
print(df.shape)
print(df[:11])


# combine data 
# loop all file in directory, append

# label data

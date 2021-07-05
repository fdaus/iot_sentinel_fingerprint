# python .\data_preparing.py 'csv_full_fingerprint'
# select 12 unique vector fingerprints
# loop all file in directory, 
# combine data, append
# save dataframe

import pandas as pd
import glob, os
import sys

from pandas.core import frame




path = sys.argv[1]


device_label=os.listdir(path)
print('device label:',device_label)

i = 1
j = 0
li = {}
while j < len(device_label):

    path_folder = path + '/' + device_label[j]
    all_files = glob.glob(path_folder + "/*.csv")
    print('path:',path_folder)
    
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None,header=None, delimiter = '\t')
        df = df.drop_duplicates()
        df = df[:12]
        li[i]= df
        print(filename)
        i+=1
    print(i)
    
    j += 1

frame = pd.concat(li, axis=0)

#save dataframe as pickle 
pickle_file = 'all_data.pkl'

frame.to_pickle(pickle_file)
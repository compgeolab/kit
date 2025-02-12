import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import zipfile

zip_path = sys.argv[1]
file_name = sys.argv[2]

data = dict()
with zipfile.ZipFile(zip_path, 'r') as zip_file:
    for file in zip_file.namelist():
        if file != 'README.md':
            data[file[:-4]] = pd.read_csv(zip_file.open(file), skiprows=5)

        

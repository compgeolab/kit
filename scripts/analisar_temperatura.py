import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import zipfile

zip_path = sys.argv[1]
file_name = sys.argv[2]

with zipfile.ZipFile(zip_path, 'r') as zip_file:
    print(len(zip_file.namelist()))
    for file in zip_file.namelist():
        if file != 'README.md':
            print(file)
            df = pd.read_csv(zip_file.open(file), skiprows=5)
            print(df)

import cv2
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np
import odc.stac
import pandas as pd
from pathlib import Path
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
import glob, os
from tabulate import tabulate

folder_path = r'C:\NASA_Cyano\data'

for path_name in glob.glob(os.path.join(folder_path, '*.csv')):
    print('Current file {}'.format(path_name))
    
    print('Reading file')
    metadata = pd.read_csv(path_name)
    
    print('Showing 2 first rows')
    print(metadata.head(n = 2))
    print('\n' * 3)
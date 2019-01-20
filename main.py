
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import random
import sys
import os

dataset= pd.read_csv('Data.csv')
X = dataset.iloc[:, 1].values
Y = dataset.iloc[:, 4].values
Agents = ["A1","A2","A3","A4","A5","A6"]
dummy = [0,0,0,0,0,0]
indeks_min = dummy.index(min(dummy))


size = len(X)

for z in range(0, size):
    dummy[z] = dataset.iloc[z,1]
    indeks_min = dummy.index(min(dummy))
    dataset.at[z,4]=Agents[indeks_min]
    

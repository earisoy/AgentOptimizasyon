# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:29:10 2019

@author: A60178
"""


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import random
import sys
import os
import math

#Find nth min number in array
def findMin(array,nthMin):
    indeks_min = array.index(min(array))
    for i in range(nthMin):
        array[indeks_min]+=1
        indeks_min = array.index(min(array))
    return array[indeks_min]

#Check if is null value 
def is_nan(x):
    return (x is np.nan or x != x)   

def detectEmptyElement(dataset, indeks):
    if is_nan(dataset.iloc[indeks,1]):
        return 1
    elif is_nan(dataset.iloc[indeks,2]):
        return 2 
    elif is_nan(dataset.iloc[indeks,3]):
        return 3
    elif is_nan(dataset.iloc[indeks,4]):
        return 4
    elif is_nan(dataset.iloc[indeks,5]):
        return 5
    else:
        return 0
    
def checkEmptyElement (dataset):
    for x in range(44):
        for y in range(11):
            if is_nan(dataset.iloc[x,y]):
                
            else:
                return 0
            

#Main starts here    

#Import datasets
dataset_1 = pd.read_csv('Group_1.csv')
dataset_2 = pd.read_csv('Group_2.csv')
nextMin=1
prevMin=0
n1 = [0 for i in range(44)]
empty=0
minRow=0

a=detectEmptyElement(dataset_2, 9)

    
    
    while checkEmptyElement(dataset_2)==1:
        
        
      for agentNo in range(0, 2):
            for x in range(0, 44):
                n1[x] = dataset_1.iloc[agentNo,x+1]
            prevMin=0
            nextMin=1
            minRow=0
            while nextMin>prevMin and detectEmptyElement(dataset_2, agentNo)!=0 and minRow<1:
                prevMin=nextMin
                minRow = findMin(n1,nextMin)
                index = n1.index(minRow)
                empty=detectEmptyElement(dataset_2,index)
                if     is_nan(dataset_2.iloc[agentNo, 1]) and empty!=0 and minRow<1 :
                       dataset_2.iloc[agentNo,1] = index+ 1
                       dataset_2.iloc[agentNo,6] = minRow
                       dataset_2.iloc[index,empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow
                elif  is_nan(dataset_2.iloc[agentNo, 2])  and (index+1)!=dataset_2.iloc[agentNo,1] and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,2] = index+1
                       dataset_2.iloc[agentNo,7] = minRow
                       dataset_2.iloc[index,empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow    
                elif  is_nan(dataset_2.iloc[agentNo, 3])  and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,3] = index+1
                       dataset_2.iloc[agentNo,8] = minRow
                       dataset_2.iloc[index,empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow        
                elif  is_nan(dataset_2.iloc[agentNo, 4])  and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and (index+1)!=dataset_2.iloc[agentNo,3] and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,4] = index+1
                       dataset_2.iloc[agentNo,9] = minRow
                       dataset_2.iloc[index, empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow
                elif  is_nan(dataset_2.iloc[agentNo, 5])  and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and (index+1)!=dataset_2.iloc[agentNo,3] and (index+1)!=dataset_2.iloc[agentNo,4]and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,5] = index+1
                       dataset_2.iloc[agentNo,10] = minRow
                       dataset_2.iloc[index, empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow
                else: 
                    nextMin+= 1
                     
    
    
    
    
    

          for agentNo in range(0, 1):
            for x in range(0, 44):
                n1[x] = dataset_1.iloc[agentNo,x+1]
            prevMin=0
            nexMin=1
            minRow=0
            while nextMin>prevMin and detectEmptyElement(dataset_2, agentNo)!=0 and minRow<1:
                prevMin=nextMin
                minRow = findMin(n1,nextMin)
                index = n1.index(minRow)
                empty=detectEmptyElement(dataset_2,index)
                if     is_nan((dataset_2.iloc[agentNo, 1]))  and empty!=0 and minRow<1 :
                       dataset_2.iloc[agentNo,1] = index+ 1
                       dataset_2.iloc[agentNo,5] = minRow
                       dataset_2.iloc[index,empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow
                elif  is_nan(dataset_2.iloc[agentNo, 2])  and (index+1)!=dataset_2.iloc[agentNo,1] and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,2] = index+1
                       dataset_2.iloc[agentNo,6] = minRow
                       dataset_2.iloc[index,empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow    
                elif  is_nan(dataset_2.iloc[agentNo, 3])  and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,3] = index+1
                       dataset_2.iloc[agentNo,7] = minRow
                       dataset_2.iloc[index,empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow        
                elif  is_nan(dataset_2.iloc[agentNo, 4])  and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and (index+1)!=dataset_2.iloc[agentNo,3] and empty!=0 and minRow<1:
                       dataset_2.iloc[agentNo,4] = index+1
                       dataset_2.iloc[agentNo,8] = minRow
                       dataset_2.iloc[index, empty] = agentNo+1
                       dataset_2.iloc[index,empty+5] = minRow
                else: 
                    nextMin+= 1
                     
    
    





#Create nth row as array
for i in range(0, 44):
    n1[i] = dataset_1.iloc[0,i+1]     




X= min(dataset_1.iloc[, :])

dataset_1.idxmin(axis=0, skipna=True)

indeks_min = dataset_1.index(min(dataset_1.iloc[0, :]))



for z in range(0, size):
    dummy[z] = dataset.iloc[z,1]
    indeks_min = dummy.index(min(dummy))
    dataset.at[z,4]=Agents[M]

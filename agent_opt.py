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
    
def checkEmptyElement (dataset, switch):
    switch=0
    for x in range(44):
        if switch==1:
            break
        else:
            for y in range(11):
                if is_nan(dataset.iloc[x,y]):
                    switch=1
                    break
    return switch
         
            

#Main starts here    

#Import datasets
dataset_1 = pd.read_csv('agent_group1.csv')
dataset_2 = pd.read_csv('agent_group2.csv')
nextMin=1
prevMin=0
n1 = [0 for i in range(44)]
empty=0
minRow=0
switch=0

a=detectEmptyElement(dataset_2, 22)

    

#First optimization
      while checkEmptyElement(dataset_2,switch)==1:
          for agentNo in range(0, 44):
                if detectEmptyElement(dataset_2, agentNo)!=0:
                    for x in range(0, 44):
                        n1[x] = dataset_1.iloc[agentNo,x+1]
                    prevMin=0
                    nextMin=1
                    minRow=0
                    while nextMin>prevMin  and minRow<1:
                        prevMin=nextMin
                        for x in range(0, 44):
                            n1[x] = dataset_1.iloc[agentNo,x+1]
                        minRow = findMin(n1,nextMin)
                        index = n1.index(minRow)
                        agentEmptyRow = detectEmptyElement(dataset_2, agentNo)
                        empty=detectEmptyElement(dataset_2,index)
                        if empty != 0 and agentEmptyRow>0 and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and (index+1)!=dataset_2.iloc[agentNo,3] and (index+1)!=dataset_2.iloc[agentNo,4]  and minRow<1:
                            dataset_2.iloc[agentNo,agentEmptyRow] = index+ 1
                            dataset_2.iloc[agentNo,agentEmptyRow+5] = minRow
                            dataset_2.iloc[index,empty] = agentNo+1
                            dataset_2.iloc[index,empty+5] = minRow
                        else:
                            nextMin+= 1
                else:
                     nextMin+= 1
    
    
#Second optimization (Each clolumn one by one)
                     
          while checkEmptyElement(dataset_2,switch)==1:
    
          for z in range(1, 6):
              for agentNo in range(0, 44):
                    if detectEmptyElement(dataset_2, agentNo) == z:
                        for x in range(0, 44):
                            n1[x] = dataset_1.iloc[agentNo,x+1]
                        prevMin=0
                        nextMin=1
                        minRow=0
                        while nextMin>prevMin  and minRow<1:
                            prevMin=nextMin
                            for x in range(0, 44):
                                n1[x] = dataset_1.iloc[agentNo,x+1]
                            minRow = findMin(n1,nextMin)
                            index = n1.index(minRow)
                            agentEmptyRow = detectEmptyElement(dataset_2, agentNo)
                            empty=detectEmptyElement(dataset_2,index)
                            if empty == z and agentEmptyRow == z and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and (index+1)!=dataset_2.iloc[agentNo,3] and (index+1)!=dataset_2.iloc[agentNo,4]  and minRow<1:
                                dataset_2.iloc[agentNo,agentEmptyRow] = index+ 1
                                dataset_2.iloc[agentNo,agentEmptyRow+5] = minRow
                                dataset_2.iloc[index,empty] = agentNo+1
                                dataset_2.iloc[index,empty+5] = minRow
                            else:
                                nextMin+= 1
                    else:
                         nextMin+= 1
                         

        
      for z in range(1, 6):
              for agentNo in range(0, 44):
                    if z % 2 == 0:
                       agentNo = 43 - agentNo   
                    if detectEmptyElement(dataset_2, agentNo) == z:
                        for x in range(0, 44):
                            n1[x] = dataset_1.iloc[agentNo,x+1]
                        prevMin=0
                        nextMin=1
                        minRow=0
                        while nextMin>prevMin  and minRow<1:
                            prevMin=nextMin
                            for x in range(0, 44):
                                n1[x] = dataset_1.iloc[agentNo,x+1]
                            minRow = findMin(n1,nextMin)
                            index = n1.index(minRow)
                            agentEmptyRow = detectEmptyElement(dataset_2, agentNo)
                            empty=detectEmptyElement(dataset_2,index)
                            if empty == z and agentEmptyRow == z and (index+1)!=dataset_2.iloc[agentNo,1] and (index+1)!=dataset_2.iloc[agentNo,2] and (index+1)!=dataset_2.iloc[agentNo,3] and (index+1)!=dataset_2.iloc[agentNo,4]  and minRow<1:
                                dataset_2.iloc[agentNo,agentEmptyRow] = index+ 1
                                dataset_2.iloc[agentNo,agentEmptyRow+5] = minRow
                                dataset_2.iloc[index,empty] = agentNo+1
                                dataset_2.iloc[index,empty+5] = minRow
                            else:
                                nextMin+= 1
                    else:
                         nextMin+= 1
        
        
    
    
    
    
    

 

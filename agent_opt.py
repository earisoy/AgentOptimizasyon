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

#Find nth  number in array
def findMax(array,nthMax):
    indeks_max = array.index(max(array))
    for i in range(nthMax):
        array[indeks_max]-=1
        indeks_max = array.index(max(array))
    return array[indeks_max]


#Check if is null value 
def is_nan(x):
    return (x is np.nan or x != x)   


#Check  is data exist
def isExist(dataset, n, log):
    log=0
    for y in range(1,6):
        if log==1:
            break
        else:
            for x in range(0,9):
                if dataset.iloc[x,y] == n+1:
                    log=1
                    break
    return log
    
#Detect empty element in row
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
    
#Check is there any null value in dataset   
    
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
                 
#Import datasets
dataset_1 = pd.read_csv('agent_group1.csv')
dataset_2 = pd.read_csv('agent_group2.csv')
dataset_3 = pd.read_csv('agent_group3.csv')
nextMin=1
prevMin=0
n1 = [0 for i in range(44)]
minSkorList=[0 for i in range(9)]
empty=0
minRow=0
switch=0  
zeroOne=0  
n=1
p=0



#initilazition (determine firs elemnt of groups)
dataset_3.iloc[0, 1] =1
for x in range(0, 44):
    n1[x] = dataset_1.iloc[0,x+1]
maxRow = findMax(n1,1)
index = n1.index(maxRow)
dataset_3.iloc[1, 1] = index+ 1   #-----------------------first and second  group started
for i in range(2,9): #--------------------------------------Other groups start
    prevMax=0
    nextMax=1
    maxRow=0
    while nextMax>prevMax  and maxRow<1:
        prevMax=nextMax
        for x in range(0, 44):
            n1[x] += dataset_1.iloc[index,x+1]
        maxRow = findMax(n1,nextMax)
        index = n1.index(maxRow)
        if (index+1)!=dataset_3.iloc[0,1] and (index+1)!=dataset_3.iloc[1,1] and (index+1)!=dataset_3.iloc[2,1] and (index+1)!=dataset_3.iloc[3,1] and (index+1)!=dataset_3.iloc[4,1] and (index+1)!=dataset_3.iloc[5,1] and (index+1)!=dataset_3.iloc[6,1] and (index+1)!=dataset_3.iloc[7,1] and (index+1)!=dataset_3.iloc[8,1]:  
            dataset_3.iloc[i, 1] = index+ 1   
        else:
            nextMax+= 1

            
#Distirubiton of other agents(Put other agent into groups one by one)
for agentNo in range(0, 44):
    minSkorList=[0 for i in range(9)]
    if isExist(dataset_3, agentNo, zeroOne ) == 0:
        for x in range(0,9): #---------------------------------------------------
            for y in range(1,6):
                if is_nan(dataset_3.iloc[x,y]) ==False:
                    dummy=int(dataset_3.iloc[x,y])
                    minSkorList[x] += dataset_1.iloc[agentNo,dummy]#-------------------------Aradaki fark en kÃ¼Ã§Ã¼k row belirleme
            minSkorList[x]=minSkorList[x] /y
        n=1
        p=0
        while n>p:
            p=n
            location=minSkorList.index(findMin(minSkorList, n))
            emptyElement=detectEmptyElement(dataset_3, location)
            if emptyElement!=0:
                dataset_3.iloc[location,emptyElement] = agentNo+1
            else:
                n+=1
                
                
                
#Add score of the agent next to them
for x in range(0,9):           
    for y in range(1,6):
          if is_nan(dataset_3.iloc[x,z]) == False:
            value=int(dataset_3.iloc[x,y])
            count=0
            topl=0
            for z in range (1,6):
                     m=int(dataset_3.iloc[x,z])
                     topl +=dataset_1.iloc[value,m]
                     count+=1
            avarage=topl/count
            dataset_3.iloc[x,y+5] = avarage

    

 

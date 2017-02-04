# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import statistics
import numpy as np

f=open("ClassDataSheet1.csv")

csv_f=csv.reader(f)
GPAlist=[]
YearofWorkExplist=[]
salary=[]
linkedinCon=[]
gotCoOp=[];
expSalary=[];
i=0
# loop to get all the required value
for row in csv_f:
    if i:
       GPAlist.append(row[1]);
       YearofWorkExplist.append(row[2]);
       salary.append(row[3]);
       gotCoOp.append(row[6]);
       linkedinCon.append(row[7]);
       expSalary.append(row[8]);
    i=i+1;
    #print(i)
    
GPAlistfloat = [float(i) for i in GPAlist]

print("min GPA ->" + min(GPAlist))
print("Max GPA ->" + max(GPAlist))
print("Median GPA ->")
print(statistics.median(GPAlistfloat))
print("Mean GPA ->")
print(statistics.mean(GPAlistfloat))

print("------for work exp---------")

print("min YearofWorkExp ->" + min(YearofWorkExplist))
print("Max YearofWorkExp ->" + max(YearofWorkExplist))
YearofWorkExplistfloat=[float(i) for i in YearofWorkExplist]

print("Median YearofWorkExp")
print(statistics.median(YearofWorkExplistfloat))
print("Mean YearofWorkExp")
print(statistics.mean(YearofWorkExplistfloat))

print("----mode---------")
print("Mode of salary->")
print(statistics.mode(salary))

print("----percentage Co op got----")

gotcoOpCount=0
notgotcoOpCount=0
for coop in gotCoOp:
    if coop == 'Y':
     gotcoOpCount=gotcoOpCount+1
    else:
     notgotcoOpCount=notgotcoOpCount+1;

print("% of students having Co/op")
print(gotcoOpCount*100/len(gotCoOp))

print("% of students not having Co/op")
print(notgotcoOpCount*100/len(gotCoOp))

print("-- linkedin Contacts")


linkedinConInt=list(map(int,linkedinCon))

#print(len(linkedinConInt))

linkedinCount=0;
for linkValue in linkedinConInt:
    if linkValue>500:
      linkedinCount=linkedinCount+1;
print("No of students with more than 500 LinkedIn contacts")        
print(linkedinCount)
expSalaryInt=list(map(int,expSalary))
q75,q25=np.percentile(expSalaryInt,[75,25])
iqr=q75-q25
print("Inter Quartile Range for the Expected Salalry Range")
print(iqr)
"""
@author: bishworup mollik
BSMRSTU
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
import threading 

##input part

n=int(input("Enter number of customer : "))
second= 0
arrival=np.random.randint(0,6,(n))
#arrival=np.array(input().split(),int)
arrival=np.sort(arrival)
servicetime=np.random.randint(1,10,(n))
#servicetime=np.array(input().split(),int)
servicebegin=[];
serviceend=[];
person=[i for i in range(1,n+1)]
status=defaultdict(list)
startexe=[1 for i in range(1,n+1)]

    
print("Random arrival time: ",arrival)
print("Random execution time: ",servicetime)

##calculation part
servicebegin.append(arrival[0]);
serviceend.append(servicebegin[0]+servicetime[0])
i=1;
while i<n:
    servicebegin.append(max(serviceend[i-1],arrival[i]))
    serviceend.append(servicebegin[i]+servicetime[i])
    i+=1

i=0
while i<n :
    print(arrival[i]," ",servicetime[i]," ",servicebegin[i]," " ,serviceend[i])
    i+=1
    


arrival=np.append(arrival, [999999]) 

serviceend=np.append(serviceend,[999999])   
print("Random arrival time: ",arrival)
print("Random execution time: ",serviceend)
   
idle =True 
t = 0
i = 0
j = 0
q = 0

while i<n or j<n:
    print(t)
    while arrival[i]==t:
        if idle==True:
             idle=False
             status[i].append("in service")
         
        else :
             q+=1;
             status[i].append("waiting")
        i+=1
        print("a",t,i,j)
    while serviceend[j]==t:
        if q==0:
            idle=True
            status[j][0]="complete"
        else:
            status[j][0]="complete"
            if j<n-1:
                status[j+1][0]="in service"
            q-=1
        j+=1
        print(t,i,j)
    print("Time :" ,t,"second") 
    for key,value in status.items():
        if len(value)>0:
            print(key+1," : ",value[0])                     

    t+=1


"""
@author: bishworup mollik
BSMRSTU
"""


import numpy as np
import matplotlib.pyplot as plt     
## Inventory system
totalday=90
 
n=int(9)
intialstock=int(4)
stock=intialstock
timeNeedArrive=int(13)
temp=[3,5]
s=temp[0]
S=temp[1]
#days=np.random.randint(1,totalday,n)
#days=np.sort(days)
#value=np.random.randint(1,5,n)
days=[18,27,36,57,63,72,75,78,87]
 
value=[4,3,2,3,1,2,3,3,4]
 
print(days)
print(value)
 

orderArrive=np.zeros(totalday+timeNeedArrive+1)
stockDetails=[]
dayValue=np.zeros(totalday+5)
 
i=0
t=1
while t<=totalday:
    while i<n and t==days[i]:
        dayValue[t]+=value[i];
        i+=1
    t+=1
 
 

day=0
while day<=totalday:
    if day%30==0 and s > stock:
        orderArrive[day+timeNeedArrive]=S-stock
 
    if orderArrive[day]>0:
        stock+=orderArrive[day]
        orderArrive[day]=0
 
    if dayValue[day]>0:
        stock-=dayValue[day]
    stockDetails.append(stock)
    day+=1
 
print(dayValue)
holdingCost=0.0
backlogCost=0.0
i=0
while i<=totalday:
    print(i,stockDetails[i])
    if(stockDetails[i]>0):
        holdingCost += stockDetails[i]
    if(stockDetails[i]<0):
        backlogCost+=abs(stockDetails[i])
    i+=1    
 
perHoldingCost=12
# perHoldingCost=int(input("Enter per holding cost :"))
perBacklogCost=30
# perBacklogCost=int(input("Enter per backlog cost :"))
print(holdingCost,backlogCost)
print("Avarage holding cost: ",holdingCost*perHoldingCost/totalday)
print("Avarage backlog cost: ",backlogCost*perBacklogCost/totalday)
 
temp=np.arange(1,90+2)
zeross=np.zeros(91)
print(temp)
print(zeross)
plt.figure()
plt.plot(temp,stockDetails, drawstyle='steps')
plt.plot(temp,zeross, drawstyle='steps')
plt.title('Step Line Plot')
plt.grid()
plt.show()
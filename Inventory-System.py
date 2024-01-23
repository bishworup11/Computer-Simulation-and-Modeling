
"""
@author: bishworup mollik
BSMRSTU
"""




import numpy as np
import time
import matplotlib.pyplot as plt     
## Inventory system
totalday=90
 
n=int(9)
intialstock=int(4)
stock=intialstock
timeNeedArrive=int(13)
S=5
s=3

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
customer=np.zeros(totalday+5)
 
i=0
t=1
while t<=totalday:
    while i<n and t==days[i]:
        dayValue[t]+=value[i];
        customer[t]+=1
        i+=1
    t+=1
 
 

day=0
customernumber=1;
while day<=totalday:
    time.sleep(0.5)
    print("Time : ",day," Day")
    print("==================== ")
    print("Before demand from customer Inventory level is ",stock)
    
    #order new item part
    if day%30==0 and s > stock:
        orderArrive[day+timeNeedArrive]=S-stock
        print("Order new item ",S-stock)
    
   #order item arrive
    if orderArrive[day]>0:
        stock+=orderArrive[day]
        orderArrive[day]=0
        print("Order aririve ",orderArrive[day])
 
    #demand from the customer part
    if dayValue[day]>0:
        stock-=dayValue[day]
        while customer[day]>0:
         print("Demand for the product from customer  ",customernumber," : ",value[customernumber-1]," items")
         customernumber+=1;
         customer[day]-=1
    else :
        print("No demand  ",)     
    print("After demand from customer invertory level : ",stock,"\n\n")
    stockDetails.append(stock)
    day+=1
 
#print(dayValue)
holdingCost=0.0
backlogCost=0.0
i=0
while i<=totalday:
   # print(i,stockDetails[i])
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
 
temp=np.arange(0,91)
zeross=np.zeros(91)
ss=[s]*91
SS=[S]*91
#print(temp)
#print(zeross)
plt.figure()
#invetory chart
plt.plot(temp,stockDetails, drawstyle='steps',color="blue")
#for Zero line
plt.plot(temp,zeross, drawstyle='steps',color="black")
#for S line
plt.plot(temp,SS, drawstyle='steps',color="Green")
#for s line
plt.plot(temp,ss, drawstyle='steps',color="red")

plt.title('Step Line Plot')
plt.xlabel('Day')
plt.ylabel('     Inventory Level                            s         S')
plt.grid()
plt.show()
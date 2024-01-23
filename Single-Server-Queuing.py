
"""
@author: bishworup mollik
BSMRSTU
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import threading 
import turtle
##################
#Turtle box##
t=turtle.Turtle()
t.hideturtle()
t.up() 
t.speed(10)
t.goto(200,-50)
t.fillcolor("red")
t.down() 
for _ in range(4):
  t.forward(100) 
  t.left(90) 
tt=turtle.Turtle()  
tt.penup() 
tt.hideturtle() 
tt.goto(0,100)

 
  
## Turtule position
tur=[]
turlastpos=250


def standingperson():
    global turlastpos
    # add new turtle
    new=turtle.Turtle()
    new.color("red")
    tur.append(new)
    
    tur[-1].hideturtle() 
    tur[-1].speed(10) 
    tur[-1].shape("turtle")
    tur[0].color("red")
    tur[-1].penup()          
    tur[-1].goto(-700, 0) 
    tur[-1].shapesize(2, 2, 1)
    tur[-1].showturtle()
    tur[-1].speed(5)
    tur[-1].goto(turlastpos,0)
    turlastpos -= 80
    

def executedperson():
    global turlastpos
    tur[0].shapesize(2, 2, 1)
    tur[0].shape("turtle")
    tur[0].color("green")
    tur[0].speed(2)
    tur[0].left(-90)
    tur[0].goto(200,-200)
    tur[0].left(-90)
    tur[0].goto(-1000,-200)
    tur.pop(0)
    for i in tur:
        x,y=i.pos()
        i.speed(3)
        i.goto(x+80,y)
    
    turlastpos+=80


##input part

n=int(input("Enter number of customer : "))
second= 0
arrival=np.random.randint(0,6,(n))
#arrival=np.array(input().split(),int)
arrival=np.sort(arrival)
servicetime=np.random.randint(1,6,(n))
#servicetime=np.array(input().split(),int)
servicebegin=[];
serviceend=[];
delay=[];
totaldelay=0;
person=[i for i in range(1,n+1)]
status=defaultdict(list)
startexe=[1 for i in range(1,n+1)]
waitq=list(range(n))
totalservicetime=0
    
print("Random arrival time: ",arrival)
print("Random service time: ",servicetime)

##calculation part
servicebegin.append(arrival[0]);
serviceend.append(servicebegin[0]+servicetime[0])
i=1;
while i<n:
    servicebegin.append(max(serviceend[i-1],arrival[i]))
    serviceend.append(servicebegin[i]+servicetime[i])
    i+=1
    
i=0
while i<n:
    delay.append(servicebegin[i]-arrival[i])    
    totaldelay+=delay[i];
    totalservicetime+=servicetime[i]
    i+=1

#i=0
#while i<n :
 #   print(arrival[i]," ",servicetime[i]," ",servicebegin[i]," " ,serviceend[i],delay[i]) 
  #  i+=1


arrival=np.append(arrival, [999999]) 

serviceend=np.append(serviceend,[999999])   
#print("Random arrival time: ",arrival)
#print("Random execution time: ",serviceend)
   
idle =True 
t = 0
i = 0
j = 0
q = 0
expect_avr_num_cust=0
last_idle_time=0
total_idle_time=0


while i<n or j<n:
    time.sleep(2)
    tt.clear()
    tt.write(t, align="left", font=("red", 25, "italic")) 
    while arrival[i]==t:
        if idle==True:
             idle=False
             status[i].append("in service")
             total_idle_time+=t-last_idle_time
         
        else :
             q+=1;
             status[i].append("waiting")
             waitq[q]=t
        i+=1
       # print("a",t,i,j)
        standingperson()
        
    while serviceend[j]==t:
        if q==0:
            idle=True
            status[j][0]="complete"
            last_idle_time=t
        else:
            status[j][0]="complete"
            if j<n-1:
                status[j+1][0]="in service"
            expect_avr_num_cust=(t-waitq[q])*q;
            q-=1
        j+=1
        executedperson()
       
        
        print(t,i,j)
    print("Time :" ,t,"second") 
    for key,value in status.items():
        if len(value)>0:
            print(key+1," : ",value[0])                     

    t+=1



print("arrinval time \t servicetime \t servicebegin \t service end   \t delay") 
i=0
while i<n :
    print(arrival[i]," \t\t\t\t ",servicetime[i],"\t\t\t\t ",servicebegin[i]," \t\t\t\t" ,serviceend[i]," \t\t\t",delay[i]) 
    i+=1
t-=1
print("\naverage delaly ",totaldelay/n)
print("\naverage servicetime ",totalservicetime/n)
print("\n Idle time ",total_idle_time)
print("\nExpected Average Number of Customers in queue",expect_avr_num_cust/t)

 #turtle.done()
turtle.bye()
turtle.Screen().bye()

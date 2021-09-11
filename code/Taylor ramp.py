import math
import random

def norm_rand(sigma,avg):
    while 1:
        u=2*random.random()-1
        v=2*random.random()-1
        r=u*u+v*v
        if r==0 or r>1:
            continue
        else:
            return u*math.sqrt(-2*math.log(r)/r)*sigma+avg
            break


gentime=0.00002#neutron generation time
h=0.0005#timestep size
l=[0,0.0127,0.0317,0.115,0.311,1.4,3.87]#initialize lambda
b=[0,0.000266,0.001491,0.001316,0.002849,0.000896,0.000182]#initialize beta
c=[0,0,0,0,0,0,0]#precursor concentration array
time=0#initialize time
timecounter=0
counter=1
n=1#initialize neutron density to 1
ni=1#variable to save previous neutron density
reactivity=0#initialize reactivity
while counter<=6:#initialize precursor concentration for each group (equilibirum state)
    c[counter]=b[counter]/l[counter]/gentime
    counter=counter+1
#calculate reactor point kenetic equation
print ("n")
while timecounter<=18000:#seconds
    reactivity=0.0007*time
    n=ni+(reactivity-0.007)/gentime*h*ni+h*(l[1]*c[1]+l[2]*c[2]+l[3]*c[3]+l[4]*c[4]+l[5]*c[5]+l[6]*c[6])#euqation 5
    counter=1
    while counter<=6:#precursor concentration time step (6 group)
        c[counter]=c[counter]+h*ni*b[counter]/gentime-h*l[counter]*c[counter] #euqation 6
        counter=counter+1
    ni=n
    time=time+h
    if timecounter%200==0:
        print (n,c[1],c[2],c[3],c[4],c[5],c[6])
    timecounter=timecounter+1
print (n)

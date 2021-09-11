import math
gentime=0.0005#neutron generation time
h=0.0001#timestep size
l=[0,0.0124,0.0305,0.111,0.301,1.14,3.01]#initialize lambda
b=[0,0.000215,0.001424,0.001247,0.002568,0.000748,0.000273]#initialize beta
c=[0,0,0,0,0,0,0,0,0]#precursor concentration array
time=0#initialize time
counter=0
n=1#initialize power or neutron density to 1
ni=1#variable to save previous power or neutron density
dndt=0
dnidt=0
dcdt=[0,0,0,0,0,0,0]
dcidt=[0,0,0,0,0,0,0]
reactivity=0#initialize reactivity
while counter<=6:#initialize precursor concentration (equilibirum state)
    c[counter]=b[counter]/l[counter]/gentime
    counter=counter+1
dnidt=(reactivity-0.006475)/gentime*ni+l[1]*c[1]+l[2]*c[2]+l[3]*c[3]+l[4]*c[4]+l[5]*c[5]+l[6]*c[6]
counter=0
while counter<=6:
    dcidt[counter]=ni*b[counter]/gentime-l[counter]*c[counter]
    counter=counter+1
while time<=10:#calculate reactor point kenetic equation
    reactivity = 0.006475 * math.sin(3.14159265 * time / 5)
    counter=0
    dndt=(reactivity-0.006475)/gentime*ni+l[1]*c[1]+l[2]*c[2]+l[3]*c[3]+l[4]*c[4]+l[5]*c[5]+l[6]*c[6]
    n=ni+dndt*h+0.5*h*(dndt-dnidt)#power tine step
    while counter<=6:#precursor concentration time step (6 group)
        dcdt[counter] = ni * b[counter] / gentime - l[counter] * c[counter]
        c[counter]=c[counter]+dcdt[counter]*h+0.5*h*(dcdt[counter]-dcidt[counter])
        counter=counter+1
    ni=n
    dnidt=dndt
    dcidt=dcdt
    time=time+h
print(n)


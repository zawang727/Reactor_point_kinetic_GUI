#!/usr/bin/env python3
import tkinter as tk



win=tk.Tk()
a=0

def read():
    gentime = 0.0005  # neutron generation time
    h = 0.0001  # timestep size
    l = [0, 0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01]  # initialize lambda
    b = [0, 0.000215, 0.001424, 0.001274, 0.002568, 0.000748, 0.000273]  # initialize beta
    c = [0, 0, 0, 0, 0, 0, 0]  # precursor concentration array
    reactivity = 0  # initialize reactivity
    time = 0  # initialize time
    timecounter = 0
    counter = 1
    n = 1  # initialize neutron density to 1
    ni = 1  # variable to save previous neutron density
    time = float(entrytime.get())
    reactivity = float(entryreactivity.get())
    var=entry1.get()
    if var!='':
        b[1]=float(var)
    var =entry2.get()
    if var != '':
        b[2]=float(var)
    var = entry3.get()
    if var != '':
        b[3]=float(var)
    var = entry4.get()
    if var != '':
        b[4]=float(var)
    var = entry5.get()
    if var != '':
        b[5]=float(var)
    var = entry6.get()
    if var != '':
        b[6]=float(var)
    var = entry7.get()
    if var != '':
        l[1]=float(var)
    var = entry8.get()
    if var != '':
        l[2]=float(var)
    var = entry9.get()
    if var != '':
        l[3]=float(var)
    var = entry10.get()
    if var != '':
        l[4]=float(var)
    var = entry11.get()
    if var != '':
        l[5]=float(var)
    var = entry12.get()
    if var !='':
        l[6]=float(var)
    var=entrygentime.get()
    if var!='':
        gentime=float(var)
    btot=b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
    while counter <= 6:  # initialize precursor concentration for each group (equilibirum state)
        c[counter] = b[counter] / l[counter] / gentime
        counter = counter + 1
    # calculate reactor point kenetic equation
    while timecounter <=time*10000:  # seconds
        n = ni + (reactivity - btot) / gentime * h * ni + h * (
        l[1] * c[1] + l[2] * c[2] + l[3] * c[3] + l[4] * c[4] + l[5] * c[5] + l[6] * c[6])  # euqation 5
        tan = (reactivity - btot) / gentime * h * ni + h * (
        l[1] * c[1] + l[2] * c[2] + l[3] * c[3] + l[4] * c[4] + l[5] * c[5] + l[6] * c[6])
        counter = 1
        while counter <= 6:  # precursor concentration time step (6 group)
            c[counter] = c[counter] + h * ni * b[counter] / gentime - h * l[counter] * c[counter]  # euqation 6
            counter = counter + 1
        ni = n
        timecounter=timecounter+1
    t.insert('end', str(n))



win.title("6 Group Reactor Point Kinetic Equation Calculation Tool ")
label1=tk.Label(win, text="Necessary Imformation:")
label7=tk.Label(win, text="Time (s):")
label8=tk.Label(win, text="Reactivity ((k-1)/k):")
label2=tk.Label(win, text="Other Imformation:")
labelFraction=tk.Label(win, text="Fraction:")
labelDecayconstant=tk.Label(win, text="Decay Constant(1/s):")
labelGenerationtime=tk.Label(win, text="Generation Time(s):")
labelgrou1=tk.Label(win, text="Group1")
labelgrou2=tk.Label(win, text="Group2")
labelgrou3=tk.Label(win, text="Group3")
labelgrou4=tk.Label(win, text="Group4")
labelgrou5=tk.Label(win, text="Group5")
labelgrou6=tk.Label(win, text="Group6")
labelnull=tk.Label(win, text="   ")
labelJA=tk.Label(win, text="Developed by Jenn An Wang at 2017")
labelresults=tk.Label(win,text="Neutron Population:")
calculate=tk.Button(win, text="Calculate", command=read)
entry1=tk.Entry(win)
entry2=tk.Entry(win)
entry3=tk.Entry(win)
entry4=tk.Entry(win)
entry5=tk.Entry(win)
entry6=tk.Entry(win)
entry7=tk.Entry(win)
entry8=tk.Entry(win)
entry9=tk.Entry(win)
entry10=tk.Entry(win)
entry11=tk.Entry(win)
entry12=tk.Entry(win)
entrygentime=tk.Entry(win)
entrystepsize=tk.Entry(win)
entrytime=tk.Entry(win)
entryreactivity=tk.Entry(win)
label1.grid(row=0,column=0)
label7.grid(row=0,column=1,sticky='E')
label8.grid(row=0,column=3,sticky='E')
label2.grid(row=1,columnspan=1)
labelFraction.grid(row=3,column=0,sticky='E')
labelDecayconstant.grid(row=4,column=0,sticky='E')
labelGenerationtime.grid(row=6,column=0,sticky='E')
labelnull.grid(row=5)
labelgrou1.grid(row=2, column=1)
labelgrou2.grid(row=2, column=2)
labelgrou3.grid(row=2, column=3)
labelgrou4.grid(row=2, column=4)
labelgrou5.grid(row=2, column=5)
labelgrou6.grid(row=2, column=6)
entrytime.grid(row=0,column=2)
entryreactivity.grid(row=0,column=4)
entry1.grid(column=1,row=3)
entry2.grid(column=2,row=3)
entry3.grid(column=3,row=3)
entry4.grid(column=4,row=3)
entry5.grid(column=5,row=3)
entry6.grid(column=6,row=3)
entry7.grid(column=1,row=4)
entry8.grid(column=2,row=4)
entry9.grid(column=3,row=4)
entry10.grid(column=4,row=4)
entry11.grid(column=5,row=4)
entry12.grid(column=6,row=4)
entrygentime.grid(column=1,row=6,sticky='E')
calculate.grid(column=3,row=7)
t = tk.Text(win,height=2,width=20)
t.grid(column=3,row=8, columnspan=1)
labelresults.grid(column=2,row=8, columnspan=1,sticky='E')
labelJA.grid(column=2,row=9,columnspan=3)
win.mainloop()

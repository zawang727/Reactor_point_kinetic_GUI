from tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()
#使用*来显示输入的内容，如果喜欢可以改为其它字符
entry['show'] = '*'
#分别使用*#$显示输入的文本内容
for mask in ['*','#','$']:
    e = StringVar()
    entry = Entry(root,textvariable = e)
    e.set('password')
    entry.pack()
    entry['show'] = mask

root.mainloop()
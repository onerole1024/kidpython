import tkinter # 引入tkinter模块，这样我们才可以去创建一个窗口


express='' # 保存最后要执行的数学表达式

def callback(func):
    global express # 引用全局变量需要加 global
    if func=='equal':
        strvar.set(eval(str(express)))
        express=strvar.get()
    elif func=='clear':
        strvar.set('0')
        express=''
    else:
        if func == 'dian':
            func =  '.'
        elif func == 'jian':
            func = '-'
        elif func == 'jia':
            func ='+'
        elif func == 'equal':
            func ='='
            
        if strvar.get()=='0' or strvar.get()=='0.0':
            val = ''
        else:
            val = strvar.get()
      
        strvar.set(str(val)+str(func))
        express = (str(express)+str(func))
                

window = tkinter.Tk() # 创建一个窗口
window.title('计算器') # 设置窗口的名字叫做 计算器
window.geometry('310x300') # 这是窗口宽310 高300
window.resizable(width=False,height=False) # 设置窗口宽和高不可以变大变小


strvar = tkinter.StringVar()
strvar.set('0')

text1 = tkinter.Button(window,bg='white',bd=2,  textvariable=strvar,font=("Arial",18),width=298,relief='ridge',state="disabled")

text1.pack(side='top')



# 数字 符号 按钮
frame = tkinter.Frame(window)
frame.pack()

tkinter.Button(frame, text="清空",width=13,height=3,command=lambda: callback('clear') ).grid(row=0,column=0)
tkinter.Button(frame, text="+",width=13,height=3,command=lambda: callback('jia') ).grid(row=0,column=1)
tkinter.Button(frame, text="-",width=13,height=3,command=lambda: callback('jian') ).grid(row=0,column=2)

tkinter.Button(frame, text="7",width=13,height=2,command=lambda: callback(7) ).grid(row=1,column=0)
tkinter.Button(frame, text="8",width=13,height=2,command=lambda: callback(8) ).grid(row=1,column=1)
tkinter.Button(frame, text="9",width=13,height=2,command=lambda: callback(9) ).grid(row=1,column=2)

tkinter.Button(frame, text="4",width=13,height=2,command=lambda: callback(4) ).grid(row=2,column=0)
tkinter.Button(frame, text="5",width=13,height=2,command=lambda: callback(5) ).grid(row=2,column=1)
tkinter.Button(frame, text="6",width=13,height=2,command=lambda: callback(6) ).grid(row=2,column=2)

tkinter.Button(frame, text="1",width=13,height=2,command=lambda: callback(1) ).grid(row=3,column=0)
tkinter.Button(frame, text="2",width=13,height=2,command=lambda: callback(2) ).grid(row=3,column=1)
tkinter.Button(frame, text="3",width=13,height=2,command=lambda: callback(3) ).grid(row=3,column=2)

tkinter.Button(frame, text="0",width=13,height=2,command=lambda: callback(0) ).grid(row=4,column=0)
tkinter.Button(frame, text=".",width=13,height=2,command=lambda: callback('dian') ).grid(row=4,column=1)
tkinter.Button(frame, text="=",width=13,height=2,command=lambda: callback('equal') ).grid(row=4,column=2)


window.mainloop() # 进入消息循环

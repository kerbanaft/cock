from tkinter import *
import time,threading

x = 125
y = 250
z = 70
b = 460
event = threading.Event()
ob = 0
lol = 9

root = Tk()
root.geometry('500x500')



#window = Tk()
root.resizable(width=False,height=False)

canv = Canvas(root,bg='#A9A9A9',width=499,height=499)
canv.create_rectangle(0,0,500,500,outline='black',width=5,fill='white')


for i in range(3):
      canv.create_line(x,0,x,30,width=5 )
      x += 125
x = 125



for i in range(3):
    canv.create_line(0,x,30,x,width=5)
    x += 125
x = 125

for j in range(3):
    canv.create_line(500,x,470,x,width=5)
    x += 125
x = 125

for j in range(3):
    canv.create_line(x,500,x,470,width=5)
    x += 125
x = 125









canv.create_oval(250,250,250,250,width=5 ) #центральная точка


def up():
    tim = int(time.strftime('%S'))
    print(tim)
    canv.pack()
    root.update()
    root.after(1000,up)



def tic ():
    global ob
    global pop








if lol == 0:
    pop = canv.create_line(250, 250, 250, 70, width=10)
elif lol != 0:
    tic()





up()
mainloop()



























#def sec():
    #watch.after(1000,sec)
    #watch['text'] = time.strftime('%H:%M:%S')

#watch = Label(window,font='Helvetica 50')

#watch.pack()
#sec()

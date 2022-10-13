from tkinter import *
import os
import time
a = 1
os.system('shutdown -s -t '+str(a))

tk = Tk()
tk.title('Выключение ПК')
tk.geometry('450x400')
text = Label()
text.place(relx = .5, rely = .1, anchor = 'c')

def timer() :
   global a
   a -= 1
   text.configure(text='Выключение пк произойдет \nчерез '+str(a)+'  секунд')
   if(a):
      tk.after(1000, timer)
   else :
      tk.destroy()

timer()
tk.mainloop()
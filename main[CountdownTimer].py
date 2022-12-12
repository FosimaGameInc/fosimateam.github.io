from distutils import command
from tkinter import *
import time

root = Tk()
root.geometry('400x300')
root.resizable(0,0)
root.config(bg='#F8F8FF')
root.title('Countdown Timer')

Label(root, text = "Countdown Timer", font = 'arial 20 bold', bg = '#F8F8FF').pack()
Label(root, font ='arial 15 bold', text = 'Time Present :', bg = '#F8F8FF').place(x=40 ,y=100)

curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'black' ,bg ='#F8F8FF')
curr_time.place(x=190 , y=100)

def clock():
  clock_time = time.strftime('%H:%M:%S %p')
  curr_time.config(text = clock_time)
  curr_time.after(1000,clock)

clock()


sec = StringVar()
Entry(root, textvariable= sec, width=2, font='arial 12').place(x=250,y=155)
sec.set('00')

mins = StringVar()
Entry(root, textvariable= mins, width=2, font='arial 12').place(x=225,y=155)
mins.set('00')

hrs = StringVar()
Entry(root, textvariable= hrs, width=2, font='arial 12').place(x=200,y=155)
hrs.set('00')


def countdown():
  times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
  while times > -1:
    minute,second = (times // 60 , times % 60)

    hour = 0
    if minute > 60:
      hour , minute = (minute // 60 , minute % 60)

    sec.set(second)
    mins.set(minute)
    hrs.set(hour)

    root.update()
    time.sleep(1)

    
    times -= 1

Label(root, font='arial 15 bold', text = 'Set a time', bg='#F8F8FF').place(x=40,y=150)
Button(root, text='Start', bd='5', command=countdown, bg = '#F8F8FF', font = 'arial 10 bold').place(x=150, y=210)

root.mainloop()
from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up =   str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="#3AA6B9")

lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg='#3AA6B9')
lab.place(x=100,y=40,height=50,width=300)

lab = Label(sp,text="Download Speed",font=("Time New Roman",20,"bold"),bg='#3AA6B9')
lab.place(x=100,y=130,height=50,width=300)

lab_down = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg='#3AA6B9')
lab_down.place(x=100,y=200,height=50,width=300)

lab = Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold"),bg='#3AA6B9')
lab.place(x=100,y=290)

lab_up = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg='#3AA6B9')
lab_up.place(x=100,y=360,height=50,width=300)

button = Button(sp,text='Check Speed',font=("Time New Roman",20,"bold"),bg="red",relief=RAISED,command=speedcheck)
button.place(x=100,y=460,height=50,width=300)


sp.mainloop()
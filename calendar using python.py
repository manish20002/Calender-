from tkinter import*
import calendar

text=calendar.calendar(2021)

root=Tk()
root.geometry("550x600")
root.title("CALENDAR 2021")
labell=Label(root,text="CALENDAR 2021",bg='dark gray',font=("time",28,'bold'))
labell.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text=text,font="consolas 10 bold")
l1.grid(row=2,column=1,padx=20)
root.mainloop()


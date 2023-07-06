from tkinter import *


window=Tk()
window.title("The Mile to KM Convertor")
# window.minsize(width=300,height=300)
window.config(padx=10,pady=15)

def M_to_KM():
    miles=float(Miles_Entry.get())
    km=miles * 1.609
    km=round(km,2)
    km_count.config(text=f"{km}")

Miles_Entry=Entry(width=10)
Miles_Entry.grid(row=0,column=1)

Miles_Label=Label(text="Miles")
Miles_Label.grid(row=0,column=2)

str=Label(text="is equal to")
str.grid(row=1,column=0)

km_count=Label(text="0")
km_count.grid(row=1,column=1)

KM_Label=Label(text="Km")
KM_Label.grid(row=1,column=2)

button=Button(text="Calculate",command=M_to_KM)
button.grid(row=2,column=1)


window.mainloop()

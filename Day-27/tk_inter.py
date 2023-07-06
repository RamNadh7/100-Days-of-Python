import tkinter

window= tkinter.Tk()
window.title("My Window")
window.minsize(width=800,height=600)

text=tkinter.Label(text="Hello World", font=("Ariel,22,bold"))
text.pack()

#changing the label
text["text"]="Hello"
text.config(text="Hello")


#Buttons
def button_clicked():
    text.config(text="Button is clicked")
    input_text=data.get()
    text.config(text=input_text)

button=tkinter.Button(text="Click Me" , command=button_clicked)
button.pack()

#Entry

data=tkinter.Entry(width=20)
data.pack()


window.mainloop()
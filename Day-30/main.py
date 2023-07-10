from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_Password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    list1=[random.choice(letters) for i in range(0,nr_letters)]
    list2=[random.choice(numbers) for i in range(0,nr_numbers)]
    list3=[random.choice(symbols) for i in range(0,nr_symbols)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list=list1 + list2 + list3
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password="".join(password_list)
    Password_Entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    Website_Search=Website_Entry.get().title()
    try:
          with open("password.json","r") as pass_file:
                data=json.load(pass_file)
    except FileNotFoundError:
          messagebox.showinfo(title="Not Found", message="No Passwords saved yet.Please save atleast one password before search.")
    else:
         try:
              search_data=data[Website_Search]
              email_data=search_data["Email"]
              password_data=search_data["Password"]
              messagebox.showinfo(title="Password Details",message=f"The Website you searched: {Website_Search}\nEmail: {email_data}\nPassword: {password_data}")
         except:
              messagebox.showinfo(title="Not Found",message="The Website you searched is not saved yet.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    Website_Det=Website_Entry.get().title()
    Email_Det=Email_Entry.get()
    Password_Det=Password_Entry.get()

    new_data={
         Website_Det:{
              "Email": Email_Det,
              "Password": Password_Det
         }
    }

    if len(Website_Det)==0 or len(Email_Det)==0 or len(Password_Det)==0:
        messagebox.showinfo(title="Missed Fields", message="You have missed entering few details. All the Fields are Mandatory")
    else:
        ok_or_not=messagebox.askokcancel(title=Website_Det, message=f"These are the Details you entered:\nEmail:{Email_Det}\nPassword:{Password_Det}\nDo you want to save these Details?")
        

        if ok_or_not:
            try:
                with open("password.json","r") as f:
                    #Read old data and update
                    data=json.load(f)
                    data.update(new_data)
            except FileNotFoundError:
                 with open("password.json","w") as f2:
                      json.dump(new_data,f2,indent=4)
            else:
                with open("password.json","w") as f1:
                    json.dump(data,f1 , indent=4)
            finally:
                    Website_Entry.delete(0, END)
                    Password_Entry.delete(0, END)

def Reset():
            Website_Entry.delete(0, END)
            Password_Entry.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #

Window=Tk()
Window.title("Password Manager")
Window.config(padx=50,pady=50,bg="white")


canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)
my_pass_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_pass_img)
canvas.grid(column=1,row=0)


Website_Label=Label(text="Website:",bg="white")
Website_Label.grid(row=1,column=0)

Email_Label=Label(text="Email/Username:",bg="white")
Email_Label.grid(row=2,column=0)

Password_Label=Label(text="Password:",bg="white")
Password_Label.grid(row=3,column=0)

Website_Entry=Entry(width=33)
Website_Entry.focus()
Website_Entry.grid(row=1,column=1,columnspan=1)

Email_Entry=Entry(width=52)
Email_Entry.insert(0, "Python@gmail.com")
Email_Entry.grid(row=2,column=1,columnspan=2)


Password_Entry=Entry(width=33)
Password_Entry.grid(row=3,column=1)

Search_Button=Button(text="Search", width=15, command=find_password)
Search_Button.grid(row=1,column=2)

Generate_Pbutton=Button(text="Generate Password",command=generate_Password)
Generate_Pbutton.grid(row=3,column=2)

Reset_button=Button(text="Reset",command=Reset)
Reset_button.grid(row=4,column=0)

Add_Button=Button(text="Add",width=44,command=save_file)
Add_Button.grid(row=4,column=1,columnspan=2)



Window.mainloop()
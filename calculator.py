#simple calculator using python 
#gui used here is tkinter

from tkinter import *

window=Tk()
#window size
window.geometry("470x470")
#window title
window.title("calculator")
#window background color
window.configure(background="#6b6d73")

#input function
def num_print(key):
    text=display.get()+key
    display.set(text)

#clear function
def clear():
    display.set("")

#equal function
def equalPress():
    try:
        total=str(eval(display.get()))
        display.set(total)
    except:
        display.set("error")



#display area

display = StringVar()
display_area = Entry(window, width=45, bd=5, textvariable=display,
                     justify="right", bg="#8f9c92",font=("italic"))
display_area.grid(row=0, column=0, columnspan=4,pady=7)

#buttons 1st row
Seven_button=Button(window,text="7",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("7"),height=3,width=8)
Seven_button.grid(row="1",column="0",padx=15,pady=20)
eight_button=Button(window,text="8",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("8"),height=3,width=8)
eight_button.grid(row="1",column="1",padx=15,pady=20)
nine_button=Button(window,text="9",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("9"),height=3,width=8)
nine_button.grid(row="1",column="2",padx=15,pady=20)

div_button=Button(window,text="/",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("/"),height=3,width=8)
div_button.grid(row="1",column="3",padx=15,pady=20)


#buttons 2nd row
four_button=Button(window,text="4",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("4"),height=3,width=8)
four_button.grid(row="2",column="0")
five_button=Button(window,text="5",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("5"),height=3,width=8)
five_button.grid(row="2",column="1")
six_button=Button(window,text="6",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("6"),height=3,width=8)
six_button.grid(row="2",column="2")

mul_button=Button(window,text="*",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("*"),height=3,width=8)
mul_button.grid(row="2",column="3",padx=15,pady=20)

#3rd row
one_button=Button(window,text="1",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("1"),height=3,width=8)
one_button.grid(row="3",column="0",pady=20)
two_button=Button(window,text="2",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("2"),height=3,width=8)
two_button.grid(row="3",column="1")
three_button=Button(window,text="3",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("3"),height=3,width=8)
three_button.grid(row="3",column="2")

subt_button=Button(window,text="-",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("-"),height=3,width=8)
subt_button.grid(row="3",column="3",padx=15,pady=20)


#4th row
zero_button=Button(window,text="0",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("0"),height=3,width=8)
zero_button.grid(row="4",column="1")
clear_button=Button(window,text="c",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=clear,height=3,width=8)
clear_button.grid(row="4",column="0")

add_button=Button(window,text="+",bg="#c7c8c9",bd=7,font=('helvetica 9 bold '),command=lambda:num_print("+"),height=3,width=8)
add_button.grid(row="4",column="2",padx=15,pady=20)

equal_button=Button(window,text="=",bg="#c7c8c9",bd=7,font=(' helvetica 9 bold '),command=equalPress,height=3,width=8)
equal_button.grid(row="4",column="3",padx=15,pady=20)


window.mainloop()
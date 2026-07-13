import  tkinter as tk
from tkinter import messagebox

#============Window Setting===========================
# Build Window
root = tk.Tk()
#specifying Title
root.title("Calculator")
# specifying Size of window
root.geometry("400x400")
#Is the Window resizable?
root.resizable(width=False, height=False)
#specifying Background color
root.configure(background="light blue")
# =====Frames=========================================
# make a frame and specifying its features
#
Row1_Frame = tk.Frame(root,width=400,height=45,padx= 5,pady= 5,bg="light yellow")
# use pack for show the frame on  root
Row1_Frame.pack(side="top",padx= 5,pady= 5)
Row2_Frame = tk.Frame(root,width=400,height=45,padx= 5,pady= 5,bg="light yellow")
Row2_Frame.pack(side="top",padx= 5,pady= 5)
# A Frame for containing Buttons
Middle_Frame = tk.Frame(root,width=400,height=200,padx= 5,pady= 5,bg="light yellow")
Middle_Frame.pack(side="top",padx= 5,pady= 5)
# A Frame for showing the result
Bottom_Frame = tk.Frame(root,width=400,height=90,padx= 5,pady= 5,bg="light yellow")
Bottom_Frame.pack(side="bottom",padx= 5,pady= 5)
# ===Variables=======================================================
First_Number =tk.StringVar()
Second_Number = tk.StringVar()
Result = tk.StringVar()

# ====Functions==========================================
# To add event after click buttons and check the exceptions
def add():
   try :
       value =float(First_Number.get()) + float(Second_Number.get())
       Result.set(str(value))
   except :
       error_message("Error")

def sub():
   try:
       value =float(First_Number.get()) - float(Second_Number.get())
       Result.set(str(value))
   except :
      error_message("Error")

def mul():
    try:
        value = float(First_Number.get()) * float(Second_Number.get())
        Result.set(str(value))
    except :
        error_message("Error")

def div():
    if Second_Number.get() == 0:
        error_message("Division zero Error")
    try:
        value =float(First_Number.get()) / float(Second_Number.get())
        Result.set(str(value))
    except :
        error_message("Error")
# To Change the result number of result label
def show_result():
    Result_Label.config(text= str(Result.get()))
# A function for checking the different type of exceptions
def error_message(ms):
    if ms == 'Error' :
        tk.messagebox.showerror("Error","Error")
    elif ms == 'Division zero Error' :
       tk.messagebox.showerror("Error","Division zero Error")
# ====Buttons===========================================
Plus = tk.Button(
    Middle_Frame,
    text="+",
    bg="light blue",
    padx= 35,
    pady= 35,
    command=add,
)
Plus.pack(side="left" , padx= 5,pady= 5)

Minus = tk.Button(
    Middle_Frame,
    text="-",
    bg="light blue",
    padx= 35,
    pady= 35,
    command=sub,

)
Minus.pack(side="right" , padx= 5,pady= 5)

Multiplication = tk.Button(
    Middle_Frame,
    text="*",
    bg="light blue",
    padx= 35,
    pady= 35,
    command=mul,

)
Multiplication.pack(side="right" , padx= 5,pady= 5)

Division = tk.Button(
    Middle_Frame,
    text="/",
    bg="light blue",
    padx= 35,
    pady= 35,
    command=div
)
Division.pack(side="left" , padx= 5,pady= 5)
# A button for show the result(=)
Result_Button = tk.Button(
    Bottom_Frame,
    bg="light blue",
    padx= 35,
    pady= 35,
    text="=",
    command=show_result,
)
Result_Button.pack(side="left" , padx= 5,pady= 5)
# ====Labels==========================================================
# Label to show the place of writing first number
Input1_Label = tk.Label(
    Row1_Frame,
    bg="light blue",
    padx= 23,
    pady= 15,
    text= " First Number :"
)
Input1_Label.pack(side="left" , padx= 5,pady= 5)
# Label to show the place of writing second number
Input2_Label = tk.Label(
    Row2_Frame,
    bg="light blue",
    padx= 15,
    pady= 15,
    text= " Second Number :"
)
Input2_Label.pack(side="left" , padx= 5,pady= 5)
# Label to show the result number
Result_Label = tk.Label(
    Bottom_Frame,
    bg="light blue",
    padx= 100,
    pady= 15,

)
Result_Label.pack(side="left" , padx= 5,pady= 5)

# ====Entry==============================================
# To get input parameters from the user
num1_Entry = tk.Entry(
    Row1_Frame,
    bg="light blue",
    width=150,
    textvariable= First_Number
)
num1_Entry.pack(side="left" , padx= 5,pady= 5)

num2_Entry = tk.Entry(
    Row2_Frame,
    bg="light blue",
    width=150,
    textvariable= Second_Number

)
num2_Entry.pack(side="left" , padx= 5,pady= 5)


# to keep the window open
root.mainloop()
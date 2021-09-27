import tkinter as tk  #for gui
from functools import partial
import random #to choose a random character
import pyperclip #to copy the password to clipboard
   
def generator(x):

    #defining a variable with all the available character
    available_characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    #length of password
    lengthinput=x
    pa=""

    #choosing random characters(number of characters that will be used for password=lengthinput) from available_characters
    for i in range(int(lengthinput)):
        password="".join(random.choices(available_characters))
        pa=pa+password
    print("\nThis Password Generator is developed by Md. Tausif Hossain\nTHANK YOU")
    
    u=copy1(pa)
    return pa



def call_result(label_result, n1):  
    num1 = (n1.get())  
    result = generator(num1) 
    label_result.config(text="Password : %s" % result)  
    return

def copy1(a):
    buttonCopy = tk.Button(root, text="Copy").grid(row=6, column=0)
    pyperclip.copy(a)
    labelNum8 = tk.Label(root, text="'Password Copied to Clipboard'").grid(row=7, column=0)
    labelNum8 = tk.Label(root, text="Developed by Md. Tausif Hossain").grid(row=30, column=1)
    

    
   
root = tk.Tk()  
root.geometry('700x200')  
  
root.title('Password Generator')
   
number1 = tk.StringVar()
  
labelNum1 = tk.Label(root, text="Enter Password Length in numbers").grid(row=1, column=0)

  
 
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=1)  
  
  
call_result = partial(call_result, labelResult, number1)  
  
buttonCal = tk.Button(root, text="Generate Password", command=call_result).grid(row=3, column=1)


  
root.mainloop()  

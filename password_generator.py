# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 20:07:39 2021

@author: USER
"""

from tkinter import *
import random
root=Tk()
root.title("Password Generator Pro")
root.geometry("400x400")

hed=Label(root,text="Password Generator Pro")
hed.place(relx=0.5,rely=0.1,anchor=CENTER)
result=Label(root)
pas=[[["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p""q","r","s","t","u","v","w","x","z"],[0,1,2,3,4,5,6,7,8,9],["!","@","#","$","%","^","&","*","(",")"]]]
def new_pas():
    capital=random.randint(0,25)
    small=random.randint(0,25)
    numbers=random.randint(0,9)
    special=random.randint(0,9)
    letter1=pas[0][0][capital]
    letter2=pas[0][3][special]
    letter3=pas[0][1][small]
    letter4=str(pas[0][2][numbers])
    print(letter1)
    result['text']="Password: pass"+letter1+letter2+letter3+letter4
    
btn=Button(root,text="Generete Password",command=new_pas)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
result.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
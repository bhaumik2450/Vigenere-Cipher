# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:40:10 2020

@author: bhaum
"""
from tkinter import *
  

import random 
import time 
import datetime 
  

root = Tk() 
  

root.geometry("1100x5000") 
  

root.title("Encryption and Decryption") 
  
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 
  
f1 = Frame(root, width = 800, height = 700, 
                            relief = SUNKEN) 
f1.pack(side = LEFT) 
  
# ============================================== 
#                  TIME 
# ============================================== 
localtime = time.asctime(time.localtime(time.time())) 
  
lblInfo = Label(Tops, font = ('helvetica', 25, 'bold'), 
          text = "Encryption and Decryption using \n Vigenère cipher", 
                     fg = "Black", bd = 10, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0) 
  
lblInfo = Label(Tops, font=('arial', 20, 'bold'), 
             text = localtime, fg = "Steel Blue", 
                           bd = 10, anchor = 'w') 
                          
lblInfo.grid(row = 1, column = 0) 
  
name = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 
 
def qExit(): 
    root.destroy() 
  

def Reset(): 
    name.set("") 
    Msg.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 
  
  

lblReference = Label(f1, font = ('arial', 16, 'bold'), 
                text = "Name", bd = 16, anchor = "w") 
                  
lblReference.grid(row = 0, column = 0) 
  
txtReference = Entry(f1, font = ('arial', 16, 'bold'), 
               textvariable = name, insertwidth = 4) 
                          
txtReference.grid(row = 0, column = 1) 
  

lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
         text = "MESSAGE", bd = 16, anchor = "w") 
           
lblMsg.grid(row = 1, column = 0) 
  
txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = Msg, insertwidth = 4) 
                  
txtMsg.grid(row = 1, column = 1) 
  
lblkey = Label(f1, font = ('arial', 16, 'bold'), 
            text = "KEY", anchor = "w") 
              
lblkey.grid(row = 2, column = 0) 
  
txtkey = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = key, insertwidth = 4) 
                  
txtkey.grid(row = 2, column = 1) 
  
lblmode = Label(f1, font = ('arial', 16, 'bold'), 
          text = "MODE(e for encrypt, d for decrypt)", 
                                bd = 16, anchor = "w") 
                                  
lblmode.grid(row = 3, column = 0) 
  
txtmode = Entry(f1, font = ('arial', 16, 'bold'), 
          textvariable = mode, insertwidth = 4) 
                    
txtmode.grid(row = 3, column = 1) 
  
lblService = Label(f1, font = ('arial', 16, 'bold'), 
             text = "The Result-", bd = 16, anchor = "w") 
               
lblService.grid(row = 2, column = 2) 
  
txtService = Entry(f1, font = ('arial', 16, 'bold'),  
             textvariable = Result, insertwidth = 4) 
                         
txtService.grid(row = 2, column = 3) 
  
# Vigenère cipher 
import base64 
  

def encode(key, clear): 
    enc = [] 
      
    for i in range(len(clear)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode())
  

def decode(key, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 
  
  
def Ref(): 
    print("Message= ", (Msg.get())) 
  
    clear = Msg.get() 
    k = key.get() 
    m = mode.get() 
  
    if (m == 'e'): 
        Result.set(encode(k, clear)) 
    else: 
        Result.set(decode(k, clear)) 
  
 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "Show Message", bg = "powder blue", 
                         command = Ref).grid(row = 7, column = 0) 
  

btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                  fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "green", 
                   command = Reset).grid(row = 7, column = 1) 
  

btnExit = Button(f1, padx = 16, pady = 8, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 10, text = "Exit", bg = "red", 
                  command = qExit).grid(row = 7, column = 3) 
  

root.mainloop() 
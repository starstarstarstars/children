from tkinter import *
def hello():
    print('hello world !')
def person(width , heigth):
    print('I am %s feet wide,%s feet high '%(width,heigth))
person(4,3)
person(heigth = 4,width = 3)
tk = Tk()
btn = Button(tk,text = 'click me',command = hello)
btn.pack()

tk = Tk()
canvas = Canvas(tk,width = 500,height = 500)
canvas.pack()
canvas.create_line(0,0,500,500)

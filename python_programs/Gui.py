##creating window

# from tkinter import *
# root=Tk() #name of the window
# root.title("window")
# root.geometry("300x300")
# root.mainloop()


##label

# from tkinter import*
# root=Tk()
# root.title("my window")
# root.geometry("300x300")
# lbl=Label(root,text="GUI python")
# lbl.pack()
# root.mainloop()


##button

# from tkinter import *
# root=Tk()
# root.title("my window")
# root.geometry("300x300")
# def click ():
#     print("OK")
# btn=Button(root,text="sumbit",command=click)
# btn.pack()
# root.mainloop()


##frame

# from tkinter import *
# root=Tk()
# root.title("my window")
# root.geometry("300x300")
# b_frame=Frame(root,bg="green",width=100,height=100)
# b_frame.pack(side=LEFT,padx=20)
# t_frame=Frame(root,bg="red",width=100,height=100)
# t_frame.pack(side=RIGHT,padx=20)
# root.mainloop() 

##


from tkinter import *
root=Tk()
root.title('my window')
root.geometry('500x500')
lbl=Label(root,text='GUI python')
lbl.pack()
def click():
    b_frame=Frame(root,bg='red',width=200,height=200)
    b_frame.pack(side=BOTTOM,pady=70)
btn=Button(root,bg='yellow',text="click here",width=10,height=2,command=click)
btn.pack(pady=20)
root.mainloop()


## adding image

from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry('1100x800')
root.title("picture window")
lbl=Label(root,font=9,fg='red',text='spiderman')
lbl.pack(pady=10)
path=PhotoImage(file='C:/Users/Python/Desktop/python_programs/pngwing.com.png')
ptr=Label(root,image=path,width=940,height=850)
ptr.pack()
root.mainloop()



##canvas

# from tkinter import *
# root=Tk()
# root.title("enter window")
# root.geometry('500x500')
# can=Canvas(root,bg='yellow',width='400',height='400')
# can.pack(pady=40)
# line=can.create_line(10,30,90,40)
# root.mainloop()

##check button


# from tkinter import *
# root=Tk()
# root.title('check button window')
# root.geometry('500x500')
# cb1=IntVar()
# cb2=IntVar()

# btn1=Checkbutton(root,text='button1',
#                  variable=cb1,
#                  onvalue=1,
#                  offvalue=0,
#                  width=10,
#                  height=4)
# btn2=Checkbutton(root,text='button2',
#                  variable=cb2,
#                  onvalue=1,
#                  offvalue=0,
#                  width=10,
#                  height=4)
# btn1.pack()
# btn2.pack()
# root.mainloop()


##radio button

# from tkinter import *
# root=Tk()
# root.title("radio button window")
# root.geometry("500x500")
# rb=StringVar(root,'2')
# rb1=Radiobutton(root,text="radio button1",variable=rb,value=1)
# rb2=Radiobutton(root,text='radio button2',variable=rb,value=2)
# rb3=Radiobutton(root,text='radio button3',variable=rb,value=3)
# rb1.pack()
# rb2.pack()
# rb3.pack()
# root.mainloop()

##text   

from tkinter import *
root=Tk()
root.title("text box")
root.geometry('500x500')
text=Text(root,fg='red',bg='yellow',width=400,height=400)
text.pack()
root.mainloop()

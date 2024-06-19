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

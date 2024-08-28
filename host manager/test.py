import tkinter as tk

# window
window = tk.Tk()
window.geometry("800x550+800+550")
window.title("Python Tkinter widget")
window.resizable(False, False)

#widget1 - Header
widget1 = tk.Label(master=window,text="NEWS")
widget1.grid(row=0,column=0)

#widget2 - Parent containing two columns
widget2 = tk.Frame(master=window,bg="yellow",width=200,height=100)
widget2.grid(row=1,column=0,ipadx=20,ipady=20)

#widget3 - left hand side of widget 2
widget3 = tk.Frame(master=widget2,bg="red",width=200,height=100)
widget3.grid(row=1,column=0)
tk.Label(widget3,text='content1')

#widget4 - right hand side of widget 3
widget4 = tk.Frame(master=widget2,bg="blue",width=200,height=100)
widget4.grid(row=1,column=1)
tk.Label(widget4,text='content2')



window.mainloop()
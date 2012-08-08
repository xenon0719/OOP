import tkinter

class Application(tkinter.Frame):

    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.config(bg="pink")
        self.pack()
        self.CreateWidgets()
        self.CreateWidgets1()
        self.CreateWidgets2()

    def CreateWidgets(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="Hello World")
        self.label1.pack()

    def CreateWidgets1(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="We are Gabriel and Ferdinand")
        self.label1.pack()
        
    def CreateWidgets2(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="Nice to meet you")
        self.label1.pack()

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()

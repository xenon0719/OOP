import tkinter

class Application(tkinter.Frame):

    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()
        self.save()
        self.load()
        
    def CreateWidgets(self):
        self.textbox1=tkinter.Text()
        self.textbox1.pack()
        self.button1=tkinter.Button()
        self.button1["command"]=self.button1_click
        self.button1["text"]="click"
        self.button1.pack()
        self.savebutton=tkinter.Button()
        self.savebutton["text"]="save"
        self.savebutton["command"]=self.save
        self.savebutton.pack()
        self.loadbutton=tkinter.Button()
        self.loadbutton["text"]="load"
        self.loadbutton["command"]=self.load
        self.loadbutton.pack()
        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]="quit"
        self.quitbutton["command"]=self.quit
        self.quitbutton.pack()
    def save(self):
        text=self.textbox1.get(0.0,tkinter.END)
        
        f=open("quote.text","w")
        f.write(text)
        f.close()
        
    def load(self):
        f=open("quote.text","r")
        text=f.read()
        self.textbox1.insert(tkinter.INSERT,text)
        
        
    def button1_click(self):
        text=self.textbox1.get(0.0,tkinter.END)
        
        print(text.upper())
        print(text.lower())
        print(text.title())

        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()

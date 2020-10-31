from tkinter import *
import Back_end as BE
from tkinter import filedialog




class mainScreen(object):
    """docstring for mainScreen"""
    def __init__(self, root):
        self.root = root

        self.MainCanvas = Canvas(width = 750, height = 520, bg = "white")
        self.MainCanvas.place(x = 0 , y = 0)

        self.COLOREDETING_label = Label(self.MainCanvas,text = 'COLOR EDITING', background = "white" ,fg = "black")
        self.COLOREDETING_label.config(font = ('arial', 25 ))
        self.COLOREDETING_label.place(x = 240 , y = 160)


        self.upload_Button = Button(self.MainCanvas, text = "Edit", bg="white" ,fg="black", width = 12,height = 3,command = self.upload)
        self.upload_Button.config(font=('arial', 15 ))
        self.upload_Button.place(x = 200, y = 230)

        self.readme_Button = Button(self.MainCanvas, text = "read me", bg="white" ,fg="black", width = 12,height = 3, command = self.readme)
        self.readme_Button.config(font=('arial', 15 ))
        self.readme_Button.place(x = 400, y = 230)

    def get_main(self):

        self.__init__(self.root)

    def readme(self):
        

        self.infCanvas = Canvas(width = 750, height = 520, bg = "white")
        self.infCanvas.place(x = 0 , y = 0)
        
        self.Back = Button(self.infCanvas, text = "Back", bg="white" ,fg="black", command = self.get_main)
        self.Back.config(font=('arial', 11 ))
        self.Back.place(x = 690, y = 470)

    def Browse(self):
        self.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
        self.pathinEntry.insert(0,self.filename)        

    def upload(self):

        self.uploadCanvas = Canvas(width = 750, height = 520, bg = "white")
        self.uploadCanvas.place(x = 0 , y = 0)

        self.COLOREDETING_label = Label(self.uploadCanvas,text = 'COLOR EDITING', background = "white" ,fg = "black")
        self.COLOREDETING_label.config(font = ('arial', 25 ))
        self.COLOREDETING_label.place(x = 263 , y = 100)

        self.pathinEntry = Entry(self.uploadCanvas, width = 50 )
        self.pathinEntry.place(x = 270 , y = 180)

        self.pathinLabel = Label(self.uploadCanvas,text = 'pathin',bg = "white")
        self.pathinLabel.config(font = ('arial', 11 ))
        self.pathinLabel.place(x = 200 , y = 180)

        self.uploadButton = Button(self.uploadCanvas, text = "Browse", bg="white" ,fg="black", command = self.Browse)
        self.uploadButton.config(font=('arial', 11 ))
        self.uploadButton.place(x = 520, y = 200)

        self.pathoutEntry = Entry(self.uploadCanvas, width = 50 )
        self.pathoutEntry.place(x = 270 , y = 280)

        self.pathoutLabel = Label(self.uploadCanvas,text = 'pathout',bg ="white")
        self.pathoutLabel.config(font = ('arial', 11 ))
        self.pathoutLabel.place(x = 200 , y = 280)

        self.okButton = Button(self.uploadCanvas, text = "Edit", bg="white" ,fg="black",width = 4, command = self.Doit)
        self.okButton.config(font=('arial', 11 ))
        self.okButton.place(x = 390, y = 330)

        self.BackButton = Button(self.uploadCanvas, text = "Back", bg="white" ,fg="black", command = self.get_main)
        self.BackButton.config(font=('arial', 11 ))
        self.BackButton.place(x = 390, y = 370)



    def Doit(self):
        BE.final_cut(self.pathinEntry.get(),self.pathoutEntry.get())
        self.get_main()



root = Tk()
root.title("COLOR EDITING")
root.geometry("750x520") #(1536x864)
root.configure(background='white')
root.resizable(False, False)
scrreen1 = mainScreen(root)
root.mainloop()

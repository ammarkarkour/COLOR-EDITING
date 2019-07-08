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


# from tkinter import *
# import  Back_end as BE 
 

# class mainScreen(object):
#     """docstring for mainScreen"""
#     def __init__(self, root):
        
#         self.root = root

#         font1 = ('Helvetica', 20 )
#         font2 = ('Helvetica', 10 )

#         self.tasksCanvas = Canvas(width = 400, height = 700, bg = "black")
#         self.tasksCanvas.place(x = 70 , y = 5)

#         self.tasks = Button(root, text = "Tasks", bg="White" ,fg="black", height = 3, width = 6,command = self.opentasks)
#         self.tasks.config(font=font2)
#         self.tasks.grid(row = 0, column = 0, pady=5)

#         self.addTask = Button(root, text = "+", bg="White" ,fg="black", height = 0, width = 3,command = self.add_task1)
#         self.addTask.config(font=font1)
#         self.addTask.grid(row = 1, column = 0, pady=5)

#         self.delete = Button(root, text = "delete", bg="White" ,fg="black", height = 3, width = 6,command = self.delet_task)
#         self.delete.config(font=font2)
#         self.delete.grid(row = 2 , column=0, pady=5)

#         self.details = Button(root, text = "details", bg="White" ,fg="black", height = 3, width = 6, command = self.tasks_details)
#         self.details.config(font=font2)
#         self.details.grid(row = 3 , column=0, pady=5)

#         self.update = Button(root, text = "update", bg="White" ,fg="black", height = 3, width = 6, command = self.update_list)
#         self.update.config(font=font2)
#         self.update.grid(row = 4 , column=0, pady=5)
        

#         self.tasksList = Listbox(self.tasksCanvas,selectmode=ACTIVE,width=32,height=27)
#         self.tasksList.place(x = 0 , y=0)
#         self.yScroll = Scrollbar(self.tasksList, orient=VERTICAL)
#         self.yScroll.grid(row=0, column=1, sticky=N+S)
#         self.xScroll = Scrollbar(self.tasksList, orient=HORIZONTAL)
#         self.xScroll.grid(row=1, column=0, sticky=E+W)
#         self.listbox = Listbox(self.tasksList,selectmode=ACTIVE,width=32,height=27, bg = "black", fg = "white",
#              xscrollcommand=self.xScroll.set,
#              yscrollcommand=self.yScroll.set)
#         self.listbox.grid(row=0, column=0, sticky=N+S+E+W)
#         self.xScroll['command'] = self.listbox.xview
#         self.yScroll['command'] = self.listbox.yview
#         self.listbox.config(font = ('Helvetica', 16, "bold" ))

#         with open("tasks.txt", "r+") as f:
#             lines = f.readlines()

#         for line in lines:
#             line_list = line.split("@")
#             self.listbox.insert(END,line_list[0])



#     def opentasks(self):
        
#         self.__init__(self.root)



#     def add_task1(self):

#         font1 = ('Helvetica', 15 )

#         self.addCanvas = Canvas(width = 400, height = 700, bg = "black")
#         self.addCanvas.place(x = 70 , y = 5)

#         self.taskname_Label = Label(self.addCanvas,text = 'What is the task name ?', background = "black",fg = "white")
#         self.taskname_Label.config(font = font1)
#         self.taskname_Label.place(x = 10 , y = 20)

#         self.taskname_Entry = Entry(self.addCanvas, width = 50 , bg = "white")
#         self.taskname_Entry.insert(0,"eg: Math Homework ")
#         self.taskname_Entry.place(x = 10 , y = 60)


#         self.deadline_Label = Label(self.addCanvas,text = 'When is it due ?', background = "black" ,fg = "white")
#         self.deadline_Label.config(font = font1)
#         self.deadline_Label.place(x = 10 , y = 100)

#         self.deadline_Entry = Entry(self.addCanvas, width = 50 , bg = "white" )
#         self.deadline_Entry.insert(0,"eg: 26/7/2019 or twenty sixth of july")
#         self.deadline_Entry.place(x = 10 , y = 140)


#         self.duration_Label = Label(self.addCanvas,text = 'How long does it take ?', background = "black" ,fg = "white")
#         self.duration_Label.config(font = font1)
#         self.duration_Label.place(x = 10 , y = 180)

#         self.duration_Entry = Entry(self.addCanvas, width = 50 , bg = "white")
#         self.duration_Entry.insert(0, "eg: 3 hours")
#         self.duration_Entry.place(x = 10 , y = 220)


#         self.coursegrade_Label = Label(self.addCanvas,text = 'What is your current grade in this course ?', background = "black" ,fg = "white")
#         self.coursegrade_Label.config(font = ('Helvetica', 11, "bold" ))
#         self.coursegrade_Label.place(x = 10 , y = 260)

#         self.coursegrade_Entry = Entry(self.addCanvas, width = 50 , bg = "white")
#         self.coursegrade_Entry.insert(0,"eg: ninty five percent or 95")
#         self.coursegrade_Entry.place(x = 10 , y = 300)


#         self.taskgrade_Label = Label(self.addCanvas,text = 'What is the task percentage ?', background = "black" ,fg = "white")
#         self.taskgrade_Label.config(font = font1)
#         self.taskgrade_Label.place(x = 10 , y = 340)

#         self.taskgrade_Entry = Entry(self.addCanvas, width = 50 , bg = "white")
#         self.taskgrade_Entry.insert(0, "eg: three percent or 3")
#         self.taskgrade_Entry.place(x = 10 , y = 400)


#         addTask = Button(self.addCanvas, text = "Add Task", bg="white" ,fg="black", height = 0, width = 8,command = self.add_task2)
#         addTask.config(font=('Helvetica', 10, "bold" ))
#         addTask.place(x = 10, y = 440)
        

#     def add_task2(self):
#         taskname = self.taskname_Entry.get()
#         deadline = self.deadline_Entry.get()
#         duration = self.duration_Entry.get()
#         taskgrade = self.taskgrade_Entry.get()
#         coursegrade = self.coursegrade_Entry.get()

#         if taskname != "eg: Math Homework " and deadline != "eg: 26/7/2019 or twenty sixth of july" and duration != "eg: 3 hours" and taskgrade != "eg: 95 percent or 95" and coursegrade != "eg: 3 percent or 3" :


#             BE.add_task(taskname,BE.get_taskScore(BE.get_duration(duration),BE.get_taskTime(BE.get_duration(duration)
#             ,BE.get_deadline(deadline)),BE.get_taskGrade(BE.get_grade(taskgrade),BE.get_grade(coursegrade)))
#             ,BE.get_deadline(deadline),BE.get_duration(duration), BE. get_grade(taskgrade), BE.get_grade(coursegrade))
            
#             self.opentasks()



#     def delet_task(self):
        
#         tasks = BE.get_tasks()
#         index = int(self.listbox.curselection()[0])
#         BE.delete_task(tasks[index][0])
#         self.opentasks()



#     def update_list(self):
        
#         BE.update_list()
#         self.opentasks()



#     def tasks_details(self):
        

#         font1 = ('Helvetica', 15 )
#         tasks = BE.get_tasks()
#         index = int(self.listbox.curselection()[0])
#         taskName = tasks[index][0]

#         for i in tasks:
#             if i[0] == taskName:
#                 line = i 

#         self.detailsCanvas = Canvas(width = 400, height = 700, bg = "black")
#         self.detailsCanvas.place(x = 70 , y = 5)

#         self.taskname_Label2 = Label(self.detailsCanvas,text = 'Task NAME :', background = "black",fg = "white")
#         self.taskname_Label2.config(font = font1)
#         self.taskname_Label2.place(x = 10 , y = 20)

#         self.taskname_Entry2 = Entry(self.detailsCanvas, width = 50 , bg = "white")
#         self.taskname_Entry2.insert(0,line[0])
#         self.taskname_Entry2.place(x = 10 , y = 60)


#         self.deadline_Label2 = Label(self.detailsCanvas,text = 'Deadline :', background = "black" ,fg = "white")
#         self.deadline_Label2.config(font = font1)
#         self.deadline_Label2.place(x = 10 , y = 100)

#         self.deadline_Entry2 = Entry(self.detailsCanvas, width = 50 , bg = "white" )
#         deadline = ((line[1].split(" "))[0]).split("-")
#         deadline = deadline[2] + "/" + deadline[1] + "/" + deadline[0]
#         self.deadline_Entry2.insert(0,deadline)
#         self.deadline_Entry2.place(x = 10 , y = 140)


#         self.duration_Label2 = Label(self.detailsCanvas,text = 'Length :', background = "black" ,fg = "white")
#         self.duration_Label2.config(font = font1)
#         self.duration_Label2.place(x = 10 , y = 180)

#         self.duration_Entry2 = Entry(self.detailsCanvas, width = 50 , bg = "white")
#         self.duration_Entry2.insert(0,line[3])
#         self.duration_Entry2.place(x = 10 , y = 220)


#         self.coursegrade_Label2 = Label(self.detailsCanvas,text = 'Course Grade :', background = "black" ,fg = "white")
#         self.coursegrade_Label2.config(font = ('Helvetica', 11, "bold" ))
#         self.coursegrade_Label2.place(x = 10 , y = 260)

#         self.coursegrade_Entry2 = Entry(self.detailsCanvas, width = 50 , bg = "white")
#         self.coursegrade_Entry2.insert(0, line[5])
#         self.coursegrade_Entry2.place(x = 10 , y = 300)


#         self.taskgrade_Label2 = Label(self.detailsCanvas,text = 'Task percentage :', background = "black" ,fg = "white")
#         self.taskgrade_Label2.config(font = font1)
#         self.taskgrade_Label2.place(x = 10 , y = 340)

#         self.taskgrade_Entry2 = Entry(self.detailsCanvas, width = 50 , bg = "white")
#         self.taskgrade_Entry2.insert(0,line[4])
#         self.taskgrade_Entry2.place(x = 10 , y = 400)


#         editTask = Button(self.detailsCanvas, text = "Edit Task", bg="white" ,fg="black", height = 0, width = 8,command = self.edit_task)
#         editTask.config(font=('Helvetica', 10, "bold" ))
#         editTask.place(x = 10, y = 440)


#     def edit_task(self):
#         taskname = str(self.taskname_Entry2.get())
#         deadline = BE.get_deadline(str(self.deadline_Entry2.get()))
#         duration = BE.get_duration(str(self.duration_Entry2.get()))
#         taskgrade = BE.get_grade(str(self.taskgrade_Entry2.get()))
#         coursegrade = BE.get_grade(str(self.coursegrade_Entry2.get()))

#         taskScore = BE.get_taskScore(duration,BE.get_taskTime(duration,deadline),BE.get_taskGrade(taskgrade,coursegrade))

#         BE.edit_task(taskname, taskScore, deadline, duration, taskgrade, coursegrade)

#         self.opentasks()

# root = Tk()
# root.title("SSA")
# root.geometry("480x720") #(1536x864)
# root.configure(background='black')
# root.resizable(False, False)
# scrreen1 = mainScreen(root)
# root.mainloop()
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
class Window(Frame):
    path = ""
    csv = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Issue Prioritizer")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance

        # placing the button on my window
        MyButton1 = Button(self, text="Add", width=10,bg="yellow",command=self.makeform)
        MyButton1.grid(row=0, column=0)

        MyButton2 = Button(self, text="Browse..",bg="yellow", width=10, command=self.load_csv)
        MyButton2.grid(row=1, column=0)

        MyButton3 = Button(self, text="Run tool..",bg="yellow", width=10, command=self.Run_tool)
        MyButton3.grid(row=2, column=0)

        MyButton4 = Button(self, text="Exit", width=10,bg="yellow", command=self.client_exit)
        MyButton4.grid(row=3, column=0)

    def Add_row(self):
        pass


    def Run_tool(self):
        pass

    def Add(self):
        toplevel = Toplevel()
        label1 = Label(toplevel, text="hii", height=0, width=100)
        label1.pack()
        label2 = Label(toplevel, text="bye", height=0, width=100)
        label2.pack()

    def makeform(self):

        I = StringVar()
        A = StringVar()
        V = StringVar()
        C = StringVar()
        retval = []
        def inner():
            global retval
            retval = [I.get(),A.get(),V.get(),C.get()]
            print(retval)
            fh = open(self.path, "a")
            app = "\n"+I.get()+","+A.get()+","+V.get()+","+C.get()+"\n"
            fh.write(app)
            fh.close()
        toplevel = Toplevel()
        form1 = Label(toplevel, text = "Issue_Description")
        form1.grid(row = 0, column = 0 )
        ent1 = Entry(toplevel, textvariable = I)
        ent1.grid(row = 0, column = 1)

        form2 = Label(toplevel, text="Assignees")
        form2.grid(row=1, column=0)
        ent2 = Entry(toplevel, textvariable=A)
        ent2.grid(row=1, column=1)

        form3 = Label(toplevel, text="Votes")
        form3.grid(row=2, column=0)
        ent3 = Entry(toplevel, textvariable=V)
        ent3.grid(row=2, column=1)

        form4 = Label(toplevel, text="Comments")
        form4.grid(row=3, column=0)
        ent4 = Entry(toplevel, textvariable=C)
        ent4.grid(row=3, column=1)

        MyButton4 = Button(toplevel, text="Submit", bg="yellow", command=inner)
        MyButton4.grid(row=4, column=0)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("TSV files", "*.tsv")))
        self.path =path
        csv = pd.read_csv(path,encoding="latin-1")
        self.csv =csv
        csv_columns = ["Issue_Description", "Assignees", "Votes", "Comments"]
        csv.columns = csv_columns
        c=1
        for i in csv.columns:
            label_1= Label(self, text= i,bg="DeepSkyBlue2")
            label_1.grid(row = 0, column = c)
            c+=1


        for index, row in csv.iterrows():
            label_1 = Label(self, text=row["Issue_Description"],bg = "white" )
            label_1.grid(row=index+1, column=1)

            label_2 = Label(self, text=row["Assignees"],bg = "white" )
            label_2.grid(row=index + 1, column=2)

            label_3 = Label(self, text=row["Votes"],bg = "white" )
            label_3.grid(row=index + 1, column=3)

            label_1 = Label(self, text=row["Comments"],bg = "white" )
            label_1.grid(row=index + 1, column=4)





    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
from tkinter import*
import pickle

class Application(Frame):
    
    txtList = []
    lblText = ["First Name", "Last Name", "Address",
               "City", "State", "Zip", "Phone Number",
               "Hourly Rate", "Normal Hours"]
    Employees = []
    currentEmp = 0
    EmployeeData = []
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.grid()
        self.create_widget()
        
        
    def Close(self):
        root.destroy()
        
    def CreateDataList(self):
        self.EmployeeData = []
        for txt in self.txtList:
            self.EmployeeData.append(txt.get())
            
    def SaveData(self):
        self.CreateDataList()
        tf = open("", "ab")
        pickle.dump(self.EmployeeData, tf)
        tf.close()
        
    def LoadData(self):
        self.currentEmp = 0
        try:
            tf = open("", "rb")
    
            while True:
                self.EmployeeData = []
                self.EmployeeData = pickle.load(tf)
                self.Employees.append(self.EmployeeData)
            tf.close()
        except EOFError:
            pass
        except FileNotFoundError:
            pass
        self.DisplayDataOnForm()
    
    def DisplayDataOnForm(self):
        self.Clear()
        try:
            for txt in self.txtList:
                txt.insert(0,self.Employees[self.currentEmp][self.txtList.index(txt)])
        except IndexError:
            pass
        
    def NextEmp(self):
        self.currentEmp +=1
        if self.currentEmp > len(self.Employees) - 1:
            self.currentEmp = len(self.Employees) - 1
        self.DisplayDataOnForm()
    def PrevEmp(self):
        self.currentEmp -= 1 
        if self.currentEmp < 0:
            self.currentEmp = 0
        self.DisplayDataOnForm()
    def FirstEmp(self):
        self.currentEmp = 0
        self.DisplayDataOnForm()
    def LastEmp(self):
        self.currentEmp = len(self.Employees) - 1
        self.DisplayDataOnForm()
    def Clear(self):
        for txt in self.txtList:
            txt.delete(0, END)
        self.txtList[0].focus()
    
    def create_widget(self):
        for i in range(9):
            entry = Entry(self)
            entry.grid(row=i + 1, column=3)
            self.txtList.append(entry)
        
        for i in range(9):
            Label(self,text=self.lblText[i]).grid(row=i + 1, column=0, pady=3, sticky = W)
            
        Button(self,text="Save",command=self.SaveData).grid(row=10,column=0)
        Button(self,text="Load",command=self.LoadData).grid(row=10, column=1)
        Button(self, text="Clear", command=self.Clear).grid(row=10, column=2)
        Button(self, text="Close", command=self.Close).grid(row=10, column=3)  
        Button(self, text="First Emp", command=self.FirstEmp).grid(row=11,column=0)
        Button(self,text="Prev Emp",command=self.PrevEmp).grid(row=11,column=1)
        Button(self,text="Next Emp",command=self.NextEmp).grid(row=11,column=2)
        Button(self,text="Last Emp",command=self.LastEmp).grid(row=11,column=3)
        
root = Tk()
root.title("New Employee Entry")
root.geometry("350x300")

app = Application(root)

root.mainloop()
from tkinter import*
import EmployeeDBSQL


class Application(Frame):
    
  
    lblText = ["Employee ID","First Name", "Last Name", "Address",
               "City", "State", "Zip", "Phone Number",
               "Hourly Rate", "Normal Hours"]
    dbColumnNames = ["EmpID", "FirstName","LastName",
                     "Address","Zip","City","State",
                        "PhoneNumber", "Rate","hours"]
   
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.grid()    
        self. txtList = []
        self.Employees = []
        self.currentEmp = 0
        self.EmployeeData = []
        self.create_widget()
        self.EmployeeDB = EmployeeDBSQL.EmployeeDBSQL()
        
    def Close(self):
        self.master.destroy()
        
    def CreateDataList(self):
        self.EmployeeData = []
        for txt in self.txtList:
            self.EmployeeData.append(txt.get())
            
    def SaveData(self):
        self.CreateDataList()
        self.EmployeeDB.InsertData(self.EmployeeData)
        
    def LoadData(self):
        self.currentEmp = 0
        self.Employees = self.EmployeeDB.getData()
        self.DisplayDataOnForm()
    
    def DisplayDataOnForm(self):
        self.Clear()
        for txt in self.txtList:
            txt.insert(0,self.Employees[self.currentEmp][self.txtList.index(txt)])
        
    def NextEmp(self):
        try:
            self.currentEmp +=1
            if self.currentEmp > len(self.Employees) - 1:
                self.currentEmp = len(self.Employees) - 1
            self.DisplayDataOnForm()
        except:
            pass
    def PrevEmp(self):
        try:
            self.currentEmp -= 1 
            if self.currentEmp < 0:
                self.currentEmp = 0
            self.DisplayDataOnForm()
        except:
            pass
    def FirstEmp(self):
        try:
            self.currentEmp = 0
            self.DisplayDataOnForm()
        except:
            pass
    def LastEmp(self):
        try:
            self.currentEmp = len(self.Employees) - 1
            self.DisplayDataOnForm()
        except:
            pass
    def Clear(self):
        for txt in self.txtList:
            txt.delete(0, END)
        self.txtList[0].focus()
    
    def deleteEmp(self):
        try:
            primaryKey = self.txtList[0].get()
            self.EmployeeDB.deleteSelection(primaryKey)
            self.LoadData()
        except:
            pass
        
    def updateEmp(self):
        
        if self.Employees != []:
            for txt in self.txtList:
                if self.txtList.index(txt) == 0:
                    continue
                if txt.get() != self.Employees[self.currentEmp][self.txtList.index(txt)]:
                    self.EmployeeDB.UpdateDB(self.currentEmp+1,
                                            self.dbColumnNames[self.txtList.index(txt)], txt.get())
        
    
    def create_widget(self):
        for i in range(10):
            entry = Entry(self)
            entry.grid(row=i + 1, column=3)
            self.txtList.append(entry)
        
        for i in range(10):
            Label(self,text=self.lblText[i]).grid(row=i + 1, column=0, pady=3, sticky = W)
             
        Button(self,text="Save",command=self.SaveData).grid(row=11,column=0)
        Button(self,text="Load",command=self.LoadData).grid(row=11, column=1)
        Button(self, text="Clear", command=self.Clear).grid(row=11, column=2)
        Button(self, text="Close", command=self.Close).grid(row=11, column=3)  
        Button(self, text="First Emp", command=self.FirstEmp).grid(row=12,column=0)
        Button(self,text="Prev Emp",command=self.PrevEmp).grid(row=12,column=1)
        Button(self,text="Next Emp",command=self.NextEmp).grid(row=12,column=2)
        Button(self,text="Last Emp",command=self.LastEmp).grid(row=12,column=3)
        Button(self,text="Delete Emp",command=self.deleteEmp).grid(row=13,column=0)
        Button(self,text="Update Emp:",command=self.updateEmp).grid(row=13,column=1)
    
import sqlite3


class EmployeeDBSQL(object):
    DBURL = "XYZCorp.db"
# Check to see if database exist; if not, create one.
    def __init__(self):
        try:
            self.__CreateDB()
        except:
            pass

# Create the database 
    def __CreateDB(self):

        conn = sqlite3.connect(self.DBURL)
        cur = conn.cursor()
        cur.execute('''create table employees (EmpID integer primary key not null,
                        FirstName text,
                        LastName text,
                        Address text,
                        Zip text,
                        City text,
                        State text,
                        PhoneNumber text,
                        Rate text,
                        hours text)''')

        conn.commit()
        conn.close()
      
#Open the database
    def OpenDB(self):
        
        conn = sqlite3.connect(self.DBURL)
        conn.close()
        
#Update values for 1 record
    def UpdateDB(self, PrimaryKey, column, feild):
        conn = sqlite3.connect(self.DBURL)
        cur = conn.cursor()
        query = "update Employees set "
        data = column + " = ? where EmpID = ?"
        cur.execute(query +data, (feild, PrimaryKey))
        conn.commit()
        conn.close()

# Delete entire selected record 
    def deleteSelection(self, primaryKey):
        
        conn = sqlite3.connect(self.DBURL)
        cur = conn.cursor()

        cur.execute("delete from Employees where empID = " + str(primaryKey))

        conn.commit()
        conn.close()

#Insert new record into Employees table 
    def InsertData(self, empDataList):
        conn = sqlite3.connect(self.DBURL)
        cur = conn.cursor()
     
       
        placeholder = ",".join(["?" for _ in empDataList])
        query ='''insert into employees (EmpID,FirstName,LastName,
        Address, Zip, City, State,PhoneNumber,Rate,Hours)Values(''' + placeholder + ")"
        
        
        cur.execute(query,empDataList)
        
            
        conn.commit()
        conn.close()
        
#Retreive data from Employees table     
    def getData(self):
        
        
        conn = sqlite3.connect(self.DBURL)
        cur = conn.cursor()

        cur.execute("select * from employees")

        row = cur.fetchone()
        data =[]
        while row != None:
            data.append(row)
            row = cur.fetchone()
    
        conn.close()
        return data
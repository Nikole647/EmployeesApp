import requests
from Employee import Employee
import json
isOpen=True
url="http://127.0.0.1:5000"

def main():
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())
        functions[choice]() #סוגריים כדי לקרוא לזה כפונקציה מהמילון

def testServer():
    print(requests.get(url+"/test").text)

def printMenu():
    print("0.Test server")
    print("1.add employee")
    print("2.get employee by Id")
    print("3.get employee by name")
    print("4.get all employee")
    print("5.update employee")
    print("6.delete employee")
    print("7.import employee from csv")
    print("8.export employees to csv")
    print("9.exit")


def addEmployee():
    details=input("Please enter: (id, firs name, last name,gender, age,salary,mail)").split(",")
    newEmp=Employee(int(details[0]),details[1],details[2],details[3],float(details[4]),float(details[5]),details[6])
    newEmpJson = json.dumps(newEmp)
    requests.post(url+'/addEmployee',json=newEmpJson)

def getEmployeeById():
    pass
def getEmployeeByName():
    pass
def getAllEmployees():
    pass
def updateEmployee():
    pass
def deleteEmployee():
    pass
def importEmployeesFromCsv():
    pass
def exportEmployeesToCsv():
    pass


functions = {
    0: testServer,
    1: addEmployee,
    2: getEmployeeById,
    3: getEmployeeByName,
    4: getAllEmployees,
    5: updateEmployee,
    6: deleteEmployee,
    7: importEmployeesFromCsv,
    8: exportEmployeesToCsv,
    9: exit
}


if __name__ == "__main__":
    testServer()
    #123,nicole,gurevich,22,fghhhhy,jnkjnjn

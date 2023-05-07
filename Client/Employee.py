class Employee:

    def __init__(self, id,first_name,last_name, gender, age, salary,email):
        self.__firstName = first_name
        self.__lastName = last_name
        self.__gender = gender
        self.__age = age
        self.__id = id
        self.__salary = salary
        self.__email = email


    def __str__(self):
        return "ID: {},first name:{},last name{},Gender:{}, Age:{} ,Salary: {},email: {}".format(self.__id,self.first_name,self.__lastName, self.__gender,self.__age,self.__salary,self.__email)


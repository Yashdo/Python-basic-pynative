
"""Use a genrator"""
# class Student:
#     def __init__(self,id,name,language,subject,marks) -> None:
        
#         self.id = id
#         self.name=name
#         self.language=language
#         self.subject=subject
#         self.marks=marks
        
#         print( id,name,language,subject,marks)
# Student(1,"yash","eng","py",45)
# Student(2,"rohit","eng","py",45)

"""Use a class"""

# class Student:
#     def student1(id,name,language,subject,marks):
#         print(id,name,language,subject,marks)
#     def student2(id,name,language,subject,marks):
#         print(id,name,language,subject,marks)
#     student1(1,"yash","eng","py",45)
#     student2(2,"rohit","eng","py",45)

"""Use a single inharitance"""

# class Student1:
#     def __init__(self,id,name,language) :
        
#         self.id = id
#         self.name=name
#         self.language=language
    
#     def info(self):

#         print(f'Student id {self.id} , Student name {self.name} , Student languages {self.language} ')

# class Student2(Student1):
#     def student(self,salary):

#         # super().__init__(id,name,language)
#         self.salary=salary

#         print(f'Student id {self.id} , Student name {self.name} , Student languages {self.language} , salary {self.salary} ')

# stu=Student2(1,"Yash","python")
# stu.student(2000)
# stu.info()

"""Multiline inharitance"""

class Company:

    def Employee(self,id,name):
        self.id=id
        self.name=name

class employee1(Company):

    def emoloyee_salary(self,salary):
        # super().Employee(salary)
        self.salary=salary
        
class employee2(employee1):

    def employee_language(self,language):
        # super().Employee(language)
        self.language = language

info=employee2()
info.Employee(1,"yash")
info.emoloyee_salary(20000)
info.employee_language("python")
print(info.id, info.name , info.salary,info.language)



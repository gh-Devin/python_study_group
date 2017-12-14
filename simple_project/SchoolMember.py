#-*- coding:utf-8 -*-

class SchoolMember:
    '''学校成员父类'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("Name:'{}' Age:'{}'".format(self.name, self.age))

class Teacher(SchoolMember):
    '''老师子类'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        print("Salary: '{0:d}'".format(self.salary))

class Student(SchoolMember):
    '''学生子类'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        print("marks: '{:d}'".format(self.marks))

t = Teacher("Mr.Devin", 40, 5000)
s = Student("erick", 23, 75)

members = [t,s]

for member in members:
    member.tell()

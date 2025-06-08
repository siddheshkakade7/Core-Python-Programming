# class : Class is considered as a blueprint of objects

# # creating a class:
# class Student:
#     x = 90
# print(Student)
#
# # Creating object:
# s1 = Student()
# print(s1.x)


# # creating a constructor:
# class Faculty:
#     def __init__(self, name, subject):
#         self.name1 = name
#         self.subject1 = subject


# f1 = Faculty(name="XYZ", subject="Python")
# print("My name is " + f1.name1 + " subject is " + f1.subject1)

# Creating a class with method :

# class Student:
#     x = 90
#
#     def stu_details(self, name, subject):
#         self.z = 10
#         self.name1 = name
#         self.subject1 = subject
#         return self.name1, self.subject1
#
# s1 = Student()
# print(s1.x)
# print(s1.stu_details("XYZ", "Python"))
# print(s1.z)


# constructor with method:

class Student:
    def __init__(self, name, subject):
        self.z = 20
        self.name1 = name
        self.subject1 = subject

    def display(self):
        print(self.name1, self.subject1)


s1 = Student("XYZ", "Python")
s1.display()

# deleting an object property:
# del s1.name1

# deleting an object :
del s1

# Pass Statement :
class Student1:
    pass

s1 = Student1()

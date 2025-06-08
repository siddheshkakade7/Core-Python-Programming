# Passing arguments

# 1) Positional Arguments(Required Arguments): no.of arguments = no. of parameter otherwise gives typeerror

# 2) Keyword / Named Arguments:

# def display(name, id):
#     print(name, name)
#
# display(id=10, name="ABC")


# # 3) Default Arguments : all arguments can be default.
#
# def display(name, age=20):                # default argument always at last position.
#     print("My name is", name, "and age is", age)
#
# display(name="SIDDHESH", age=21)


# Variable - Length Arguments :

# def my_function(*course_name):
#     print(course_name)
#     print("The new course is" + course_name[0] + "\t")
#
# my_function("Python", "Java", "PHP")

# def my_function(*course_name):
#     print(course_name)
#     for i in course_name:
#         print("The new course is " + i)
#
# my_function("Python", "Java", "PHP")

# # Passing a list as an argument
#
# def my_list(l2):
#
#     for i in l2:
#         print(i)

# l1 = [1, 2, 3, 4, 5, 6]
# my_list(l1)
# print(l1)

# pass

def add():
    pass
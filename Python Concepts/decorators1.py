# function can store a variable
# def fun1():
#     print("Hello")
#
# # fun1()  # function call
#
# a = fun1   # function assignment
# print(a)
# a()


# def fun1(text):
#     a = text.upper()
#     return a
#
# def fun2(func):
#     print(func)
#     greet = func("hi, its 3ri")
#     print(greet)
# fun2(fun1)

# Returning function from another function.
#
# def fun1(text):
#     a = text.upper()
#     return a
#
# def fun2():
#     print("Its fun 2")
#     return fun1
#
# x = fun2()
# print(x)
# print(x("hi, its 3ri."))

# # function modification
# def dec(func):
#     def fun2():
#         print("Its an It Institute ")
#         func()
#         print("Hii")
#
#     return fun2
#
# def fun1():
#     print("3RI")
#
# fun1 = dec(fun1)
# fun1()

# # function modification
# def dec(func):
#     def fun2():
#         print("Its an It Institute ")
#         func()
#         print("Hii")
#
#     return fun2
#
# def fun1():
#     print("3RI")


# def dec(func):
#     print("Im in dec..")
#     print(func)
#
#     def fun2():
#         func()
#
#         print("It is an Institute")
#
#     return fun2
#
#
# @dec
# def fun1():
#     print("3RI")

#
def cal(fun):
    print("What to calculate ?", fun)
    fun()

    def add():
        x = int(input("Enter No. :"))
        y = int(input("Enter No. :"))
        print(x + y)

    return add

@cal
def sum():
    x = int(input("Enter No. :"))
    y = int(input("Enter No. :"))
    print(x - y)

sum()
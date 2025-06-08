# # Global Variables :
# x = "Hello"
# def greet():
#     print(x, "this is Python.")
#
# greet()
# print(x)           # globally called

# Local Variables :

# def greet():
#     x = "Hello"
#     print(x, "this is Python.")
#     print(x)                # Locally called
#
# greet()
# print(x)           # error

# # If we created two variables with same name inside and outside a function, both variable work in their scope.
#
# x = "Hello"
# def greet():
#     x = "Hi"
#     print(x, "this is Python.")
#
# greet()
# print(x, "this is Python.")

# # Global Keyword :
#
# def greet():
#     global x
#     x = "Hello"
#     print(x, "this is Python.")
#
# greet()
# print(x, "this is Java.")

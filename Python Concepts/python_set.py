# Python Set :
# Unordered collection of data

# Creating a set
# days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# print(days)
# print(type(days))

# Using set()
# set constructor()
# s1 = set(("a", "b", "c", "d")) # print(s1)
# print(len(s1))  # length

# Access set elements
# for x in days:
#     print(x)

# calculating length without len()
# x = 0
# for i in days:
#     x = x + 1
# print(x)

# # Adding items to set
# s = {1, 2, 3, 4, 5, 6}
# s.add(10)   # for single value
#
# s.update([12, 11])  # for multiple value
# print(s)

# # Removing items from
s = {"a", "b", "c", "d", "e"}

# # Discard()
# s.discard("4")
# print(s)

# # Remove()
# s.remove("a")
# print(s)

# # pop()
# s.pop()
# print(s)
# i = s.pop()
# print(i)

# # clear ()
# s.clear()
# print(s)

# # del
# del s
# print(s)

# operations on set ()

# # union()
D1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
D2 = {"Friday", "Saturday", "Sunday"}
# print(D1 | D2)

# print(D1.union(D2))

# # intersection()
#
# print(D1 &(D2))
# print(D1.intersection(D2))

# # difference
# print(D1.difference(D2))
# print(D1 - D2)

# # Symmetric_Difference
# print(D1.symmetric_difference(D2))
# print(D1 ^ D2)

# # read():

# a = open("basic.py", "r")
# print(a.read())

# f = open("D:/Python/try.txt", "r")
# print(f.read(10))

# readline()
# print(f.readline())
# print(f.readline())

# readlines()
# content = f.readlines()
# print(content)
# print(content[1])

# for i in range(3):
#     print(content[i])

# close files
# f.close()
# print(f.close())

# # Write():
# f = open("try.txt", "a")
# f.write("Now the file has more contents !!!")

# f = open("try.txt", "w")
# f.write("Now the file has more contents !!! With write mode.")   # deletes already existing data and add content.

# f = open("try1.txt", "x")
# f.write("Its a new file with data !!!!")

# import os
# # os.remove("try1.txt")
# if os.path.exists("try.txt"):
#     os.remove("try.txt")
#
# else:
#     print("File Does Not Exist...")
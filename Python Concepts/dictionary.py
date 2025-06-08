# Dictionary
# values stored in key-value pairs

dict1 = {"Brand": "Nissan", "Model": "Skyline", "Year": "2020"}
# print(dict1)
# print(type(dict1))
# print(dict1["Brand"])
#
# # Replacing
# dict1['Model'] = "R"
# print(dict1)
#
# # Adding Items
# dict1["Price"] = '5M'
# print(dict1)
#
# # Duplication not allowed
# dict1['Year'] = '2024'
# print(dict1)
#
# # length of dictionary
# print(len(dict1))

# Accessing Items
# print(dict1['Price'])
# print(dict1.get('Price'))

# # Dict() Constructor
# dict2 = dict(Name="Siddhesh", Age=20, Address="Pune")
# print(dict2)

# keys() & values()
# x = dict1.keys()
# print("Keys Of dict1 :", x)
# y = dict1.values()
# print("Values Of dict1 :", y)

# a = dict2.keys()
# print("Keys Of dict2 :", a)
# b = dict2.values()
# print("Keys Of dict2 :", b)
#

# Items ()
# x = dict1.items()
# print("Items of dict1 :", x)
# y = dict2.items()
# print("Items of dict2 :", y)

# Membership Operator
# if 'Brand' in dict1:
#     dict1["Brand"] = "GTR"   # If present then replace it
#     print(dict1)


# update dictionary :

# dict2.update({"Age": 21})
# print(dict2)

# Removing
# pop ()
# dict1.pop("Year")
# x = dict1.pop("Year")
# print(x)
# print(dict1)

# # pop items()
# x = dict1.popitem()
# print(x)
# print(dict1)

# # del()
# del dict1["Brand"]  # It not returns value as it is a keyword and others are functions
# print(dict1)

# # clear ()
# dict2.clear()
# print(dict2)

# Loop in Dictionary
# for x in dict1.values():
#     print(x)

# for x in dict1.keys():
#     print(x)

# for x, y in dict1.items():
#     print(x, y)

# Copy of a dict :
# mydict = dict1.copy()
# print(mydict)
# mydict = dict(dict1.copy())
# print(mydict)

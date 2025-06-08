# Metacharacters
import re
txt = "Hello welcome to 3RI."

# 1) [a-z] = finds all character alphabetically between given range.
# x = re.findall("[a-e]", txt)
# print(x)

# 2) (.) : any character
# x = re.findall("He..", txt)
# print(x)

# 3) ^ : starts with
# x = re.findall("^Hello", txt)
# if x:
#     print("Yes.")
# else:
#     print("No.")

# 4) $ : ends with
# x = re.findall("3RI.$", txt)
# if x:
#     print("Yes string ends with")
# else:
#     print("No.")

# 5) * : zero or more occurrence
# x = re.findall("He.*o", txt)
# print(x)

# Special Sequence
# \d = checks for digit
# x = re.findall("\d", txt)
# print(x)

# \s = returns spaces
# x = re.findall("\s", txt)
# print(x)

# [arn]
# x = re.findall("[aomn]", txt)
# print.(x)

# [^arn]
# x = re.findall("[^arom]", txt)
# print(x)

# pattern = re.compile("Hello")
# print(pattern)
# string = 'Hello World!'
# result = pattern.match(string)
# print(result)


# # pattern = re.compile("Hello", re.IGNORECASE)    # case-sensitivity
# print(pattern)
# string = 'hello World!'
# result = pattern.match(string)
# print(result)
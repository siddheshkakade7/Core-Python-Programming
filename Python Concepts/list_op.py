# list : count
# l = [31,21,34,44,5,54,5,6,5,5,5,"iiii"]
# print(type(l))
# print(l.count(5))

# index()
# print(l.index(5,1,))
# print(l.index(5))

l1 = list((1, 2, 3, 45, 5, 45, 1, 45))
print(l1)
# pop()
# print(l1.pop())
# print(l1)

# min()
# m1 = min(l1)
# print(m1)

# max()
# m2 = max(l1)
# print(m2)

# del()
# del l1[1]
# print(l1)

# reverse ()
# l1.reverse()
# print(l1)

# sort()
# l1.sort()
# print(l1)
# l1.reverse()     # descending
# print(l1)

# Print a list with user input in range of 5
l2 = []
print(type(l2))

for i in range(5):
    x = int(input("Enter Values :"))
    l2.append(x)

print(l2)

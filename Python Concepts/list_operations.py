# List Operations
l1=[1,2,3,4,5,3,43,4]
print(len(l1))
print(l1[1:3])   # Slicing operator
print(l1[:3])
print(l1[1:])
l3=list(("Apple","Cherry","Banana"))
print(l3)

l2=["abhi",2,3,4]
print(type(l2))
print(l2)
print(id(l2))
l2[0] = 20
print(l2)   # Changing Element
l2[1:3] = [3,3]
print(l2)
print(id(l2))
print(len(l2))

# repetition operator
print(l2 * 2)

# Concatenation Operator
print( l3 + l2)

# Membership Operators
print(2 in l2)
print(2 not in l2)

# loop
x = 0
for i in l1:
  #  print(i)
    x = x+1
print(x)


# Updating List

l4 = [11,2,13,15,6]
l5 = [23,12,34,12]

l4.append(8)
print(l4)

l5.insert(2,23)
print(l5)

l2.extend(l3)
print(l2)

l6 = [15,61,51,1,1]
print("Sum is :",sum(l6))

# without using sum function
add = 0
for i in l6:
     add = add + i
print("Addition of all elements is ",add)


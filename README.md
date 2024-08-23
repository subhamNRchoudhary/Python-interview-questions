# Python-interview-questions
All questions for big and midcap company

Set Function
  ( What is a set type in Python? ) 
  Python’s built-in set type has the following characteristics: Sets are unordered. Set elements are unique. Duplicate elements are not allowed. A set itself may be modified, but the elements contained in the set 
  must be of an immutable type.
  ![image](https://github.com/user-attachments/assets/95255803-973a-4d2d-b6c2-93caface9227)


The Difference between List, Tuple, Set, and Dictionary

![image](https://github.com/user-attachments/assets/0e0de444-b7b2-4547-96e0-03ea62328524)

# Python3 program for explaining
# use of list, tuple, set and 
# dictionary

# Lists
l = []

# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)

# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

# Set
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

# Tuple
t = tuple(l)

# Tuples are immutable
print("Tuple", t)
print()

# Dictionary
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)

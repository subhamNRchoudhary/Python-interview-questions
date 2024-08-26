# Python-interview-questions
*All questions for big and midcap company*

![image](https://github.com/user-attachments/assets/f766ea1e-3bc1-4791-91a4-80cdea5704c8)

*Palindrome*
A word, phrase, or sequence that reads the same backward as forwards, e.g. *madam*

![image](https://github.com/user-attachments/assets/e779de78-9c69-446e-89e1-e3b801025048)
![image](https://github.com/user-attachments/assets/54c055ad-32a0-4ec3-a976-938b3fab2cfb)




*Set Function*

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

# Adding Element into the list
	l.append(5)
	l.append(10)
	print("Adding 5 and 10 in list", l)

# Popping Elements from the list
	l.pop()
	print("Popped one element from list", l)
	print()

# Set
	s = set()

# Adding element into the set
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

# Adding the key-value pair
	d[5] = "Five"
	d[10] = "Ten"
	print("Dictionary", d)

# Removing key-value pair
	del d[10]
	print("Dictionary", d)

Lists:

Syntax: []
	Ordered: Yes (Maintains the insertion order)
 
	Mutable: Yes (Elements can be changed)
	Duplicates: Yes (Allows duplicate elements)
	Example: [1, 2, 3, 4]
Tuples:

Syntax: ()
	Ordered: Yes (Maintains the insertion order)
 
	Mutable: No (Elements cannot be changed once assigned)
	Duplicates: Yes (Allows duplicate elements)
	Example: (1, 2, 3, 4)
Sets:

Syntax: {} or set()
	Ordered: No (No guarantee of order in Python versions before 3.7)
 
	Mutable: Yes (Elements can be added or removed)
	Duplicates: No (Does not allow duplicate elements)
	Example: {1, 2, 3, 4}
Dictionaries:

Syntax: {key: value}
	Ordered: Yes (Maintains the insertion order starting from Python 3.7)
 
	Mutable: Yes (Keys and values can be changed)
	Duplicates: No (Keys must be unique, but values can be duplicated)
	Example: {'a': 1, 'b': 2, 'c': 3}

 Write a code Backwards with a space after each letter

 	a = ' '.join('sunny')
	a= a[::-1]
	print(a)

 Sum up the Last 2 Digit

 	a = '123456'
	b = int(a[-2]) + int(a[-1])
	print(b)

Identifying the Most Frequent Letter in a Word Using Python

 	from collections import Counter
	a = input('word:')  
	b = Counter(a)
	frequency = b.most_common(1)[0]
	print(frequency)
 
identifying / Counting all the letter

	from collections import Counter
	a = input('word: ')  
	b = Counter(a)
	for c,d in b.items():
	print(f"{c}={d}")

 ![image](https://github.com/user-attachments/assets/bddf0197-a4a9-42c6-b6c9-4ab528f85e62)

sorting 

	a = '55032658112365'
	b = (sorted(a))
	print(b)
---
	a = '55032658112365'
	b = sorted(a , reverse = True)
	print(b)

a)	Reverse a string.

		a = '55032658112365'
		b = sorted(a , reverse = True)
		print(b)
  --

	  a = '1856224'
	  b = '' # Initialize an empty string to store the reversed string
	  for i in range(len(a)-1,-1,-1): # Loop through the original string starting from the 						#last character to the first
	  b += a[i]  # Append the character at position 'i' to 'reversed_string'
	  print(b)


b)	Find the maximum element in an array.

	a = [5,9,2,5,66,25,75]
	b = max(a)
	b
 ----

	a = [5,9,2,5,66,25,75]
	
	# Function to find the maximum value 
	def max_value(a):
	  b_max = a[0] # Assume the first element is the maximum
	  for num in a:
	    if num > b_max: # If the current number is greater than max_value
	      b = num  # Update max_value
	  return b
	
	b = max_value(a) 
	print("max :",b)   

 
c)	Check if a string is a palindrome.
d)	Find the missing number in an array.
e)	Find the intersection of two arrays.
f)	Remove duplicates from an array.
g)	Count the occurrence of each element in an array.
h)	Find the second largest element in an array.
i)	Merge two sorted arrays.
j)	Find the length of the longest substring without repeating characters.
k)	Reverse a linked list.
l)	Implement a stack using an array.
m)	Implement a queue using an array.
n)	Find the lowest common ancestor in a binary tree.
o)	Check if a binary tree is a binary search tree.
p)	Find the level order traversal of a binary tree. 
q)	Find the Kth largest element in an array

 

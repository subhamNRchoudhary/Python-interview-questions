# Python-interview-questions
*All questions for big and midcap companies*

![image](https://github.com/user-attachments/assets/f766ea1e-3bc1-4791-91a4-80cdea5704c8)

*Palindrome*
	A word, phrase, or sequence that reads the same backward as forwards, e.g. *madam*

![image](https://github.com/user-attachments/assets/e779de78-9c69-446e-89e1-e3b801025048)
![image](https://github.com/user-attachments/assets/54c055ad-32a0-4ec3-a976-938b3fab2cfb)




*Set Function*

  ( What is a set type in Python? )
  
 	 Python’s built-in set type has the following characteristics: Sets are unordered. Set elements are unique. Duplicate elements are not allowed. A set itself may be modified, 	but the elements contained in the set 
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

 ![image](https://github.com/user-attachments/assets/2df2a268-9869-4a98-b71a-5e58e4477779)


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

*sorting*

	a = '55032658112365'
	b = (sorted(a))
	print(b)
---
	a = '55032658112365'
	b = sorted(a , reverse = True)
	print(b)

*a)	Reverse a string.*

		a = '55032658112365'
		b = sorted(a , reverse = True)
		print(b)
  --

	  a = '1856224'
	  b = '' # Initialize an empty string to store the reversed string
	  for i in range(len(a)-1,-1,-1): # Loop through the original string starting from the 						#last character to the first
	  b += a[i]  # Append the character at position 'i' to 'reversed_string'
	  print(b)


*b)	Find the maximum element in an array.*

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

 
*c)	Check if a string is a palindrome.*

	def is_palindrome(s):
	    # Remove any spaces and convert the string to lowercase for accurate comparison
	    s = s.replace(" ", "").lower()
	    return s == s[::-1]
	
	b = "A man a plan a canal Panama"
	if is_palindrome(b):
	    print("Palindrome.")
	else:
	    print("Not a Palindrome.")

![image](https://github.com/user-attachments/assets/1f2520c3-1dfa-4326-baed-c196549a6bab)
![image](https://github.com/user-attachments/assets/0688caeb-707e-4ad4-80f5-194aaf5e9520)

    
d)	Find the missing number in an array.

e)	Find the intersection of two arrays.
f)	Remove duplicates from an array.

	def remove_duplicates(a):
	return list(set(a)) # By converting the array to a set, duplicates are removed.
	# Example usage
	a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] #Converting the set back to a list gives the final array without duplicates.
	result = remove_duplicates(arr)
	print(result)

 

g)	Count the occurrence of each element in an array.

		from collections import Counter
		def count_occurrences(arr):
		    return Counter(arr)
		
		arr = [1, 2, 2, 3, 4, 4, 4, 5]
		print(count_occurrences(arr))
  ----
  

h)	Find the second largest element in an array.

	def second_largest(arr):
	    unique_arr = list(set(arr))  # Remove duplicates
	    unique_arr.sort(reverse=True)
	    return unique_arr[1] if len(unique_arr) > 1 else None
	
	arr = [3, 1, 5, 2, 4, 5, 3]
	print(second_largest(arr))

i)	Merge two sorted arrays.

	def merge_sorted_arrays(arr1, arr2):
	    return sorted(arr1 + arr2)
	
	arr1 = [1, 3, 5, 7]
	arr2 = [2, 4, 6, 8]
	print(merge_sorted_arrays(arr1, arr2))

j)	Find the length of the longest substring without repeating characters.

	def longest_substring(s):
	    char_index = {}
	    start = max_len = 0
	    for i, char in enumerate(s):
	        if char in char_index and char_index[char] >= start:
	            start = char_index[char] + 1
	        char_index[char] = i
	        max_len = max(max_len, i - start + 1)
	    return max_len
	
	s = "abcabcbb"
	print(longest_substring(s))

k)	Reverse a linked list.

	class Node:
	    def __init__(self, value):
	        self.value = value
	        self.next = None
	
	def reverse_linked_list(head):
	    prev = None
	    current = head
	    while current:
	        next_node = current.next
	        current.next = prev
	        prev = current
	        current = next_node
	    return prev
	
	# Helper function to print linked list
	def print_list(head):
	    current = head
	    while current:
	        print(current.value, end=" -> ")
	        current = current.next
	    print("None")
	
	# Example usage
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head = reverse_linked_list(head)
	print_list(head)

l)	Implement a stack using an array.

	class Stack:
	    def __init__(self):
	        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

	# Example usage
	stack = Stack()
	stack.push(10)
	stack.push(20)
	print(stack.pop())  # 20
	print(stack.peek())  # 10

m)	Implement a queue using an array.

	class Queue:
	    def __init__(self):
	        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

	# Example usage
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	print(queue.dequeue())  # 1
	print(queue.dequeue())  # 2

n)	Find the lowest common ancestor in a binary tree.
o)	Check if a binary tree is a binary search tree.
p)	Find the level order traversal of a binary tree. 
q)	Find the Kth largest element in an array

	import heapq
	
	def kth_largest(arr, k):
	    return heapq.nlargest(k, arr)[-1]
	
	arr = [3, 2, 1, 5, 6, 4]
	k = 2
	print(kth_largest(arr, k))  # 5

r) 	Find the minimum element in an array.

	a = [5,9,2,5,66,25,75]
	b = min(a)
	b
 ---
 
	a = [99, 5, 66, 3, 66]
	def minimum_value(a):
	    b_min = a[0]  # Start by assuming the first element is the minimum
	    for num in a:
	        if num < b_min:  # If the current number is smaller than b_min
	            b_min = num  # Update b_min to be the new minimum
	    return b_min  # Return the minimum value found

### 1. **What are the different data types in Python?**
   Python has various built-in data types, including:
   - **int** (Integer)
   - **float** (Floating point number)
   - **str** (String)
   - **list** (Mutable collection of items)
   - **tuple** (Immutable collection of items)
   - **dict** (Key-value pairs, mutable)
   - **set** (Unordered, unique collection of items)

### 2. **What is the difference between mutable and immutable objects in Python?**
   - **Mutable objects**: Can be changed after their creation (e.g., lists, dictionaries, sets).
   - **Immutable objects**: Cannot be changed once created (e.g., strings, tuples, integers).

### 3. **How does Python manage memory?**
   Python handles memory through its **memory manager**, which allocates memory to objects. Python also uses a **garbage collector** to remove objects that are no longer in use (using reference counting and cyclic garbage collection).

### 4. **What is the difference between a normal function and a lambda function in Python?**
   - **Normal function**: Defined using `def` and can have a block of multiple statements.
   - **Lambda function**: A short, anonymous function defined using the `lambda` keyword, typically for single-line expressions.
   
   Example:  
   `def add(x, y): return x + y`  
   `lambda x, y: x + y`

### 5. **What are global, local, and nonlocal variables in Python?**
   - **Global variables**: Defined outside any function, accessible anywhere in the code.
   - **Local variables**: Defined inside a function, accessible only within that function.
   - **Nonlocal variables**: Used in nested functions to refer to variables from the nearest enclosing scope (excluding global scope).
   
   The `global` and `nonlocal` keywords are used to refer to variables outside the current scope.

### 6. **Explain Object-Oriented Programming (OOP) concepts in Python.**
   - **Inheritance**: Allows a class to inherit properties from another class.
   - **Polymorphism**: Enables using a single interface to represent different types of objects.
   - **Encapsulation**: Bundling the data (variables) and methods that work on the data into a single unit (class).
   - **Abstraction**: Hiding internal implementation details and exposing only necessary functionalities.

### 7. **What are decorators in Python?**
   Decorators are functions that modify the behavior of another function or class. They are applied using the `@decorator` syntax. Decorators are commonly used for tasks like logging, access control, and memoization.
   
   Example:
   ```python
   @decorator_function
   def some_function():
       pass
   ```

### 8. **What are generators and iterators in Python?**
   - **Iterator**: An object that implements the iterator protocol (`__iter__` and `__next__` methods).
   - **Generator**: A special type of iterator created using the `yield` keyword, which allows values to be returned one at a time.

   Example:
   ```python
   def simple_generator():
       yield 1
       yield 2
       yield 3
   ```

### 9. **What are list comprehensions, and why are they used?**
   List comprehensions provide a concise way to create lists based on existing lists or iterables. They are faster and require fewer lines of code compared to loops.
   
   Example:
   ```python
   squares = [x**2 for x in range(10)]
   ```

### 10. **How does Python handle exceptions?**
   Exceptions are handled using the `try`, `except`, `else`, and `finally` blocks. Python raises exceptions during runtime errors, and they can be caught and handled to prevent program termination.

   Example:
   ```python
   try:
       1 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero")
   finally:
       print("End of block")
   ```

### 11. **What are modules and packages in Python?**
   - **Module**: A single Python file containing functions, classes, or variables.
   - **Package**: A collection of modules organized in directories with an `__init__.py` file.

   Example:  
   Importing a module: `import math`  
   Importing a function from a module: `from math import sqrt`

### 12. **What is a virtual environment in Python, and why is it used?**
   A virtual environment isolates Python dependencies for different projects. This prevents conflicts between package versions used in different projects.

   To create a virtual environment:
   ```bash
   python -m venv myenv
   ```

### 13. **What is the Global Interpreter Lock (GIL) in Python?**
   The GIL is a mutex in CPython that allows only one thread to execute at a time, even in a multi-threaded application. This affects the performance of CPU-bound tasks in multi-threading but not I/O-bound tasks.

### 14. **How is file handling done in Python?**
   Python uses built-in functions to handle files, such as `open()`, `read()`, `write()`, and `close()`. Files can be opened in modes like `r` (read), `w` (write), and `a` (append).

   Example:
   ```python
   with open("file.txt", "r") as file:
       content = file.read()
   ```

### 15. **What is the difference between multi-threading and multi-processing in Python?**
   - **Multi-threading**: Involves multiple threads running within a single process (limited by the GIL).
   - **Multi-processing**: Involves multiple processes, each with its own Python interpreter and memory space, bypassing the GIL.

### 16. **What is the difference between shallow copy and deep copy in Python?**
   - **Shallow copy**: Creates a new object but doesn't recursively copy nested objects.
   - **Deep copy**: Recursively copies all objects, including nested ones.
   
   The `copy` module provides `copy()` (shallow) and `deepcopy()` (deep).

### 17. **What causes memory leaks in Python, and how can they be avoided?**
   Memory leaks occur when objects are not properly garbage-collected due to circular references or keeping references to unused objects. Using weak references (`weakref` module) and careful resource management can prevent memory leaks.

### 18. **What are dunder (magic) methods in Python?**
   Dunder methods are special methods with double underscores (e.g., `__init__`, `__str__`, `__repr__`, `__add__`) that define the behavior of objects. They allow customizing object creation, representation, arithmetic operations, etc.

   Example:  
   `__str__` defines the string representation of an object.

### 19. **What are context managers, and how are they implemented in Python?**
   Context managers ensure proper acquisition and release of resources using the `with` statement. The `__enter__()` and `__exit__()` methods are used to define behavior when entering and exiting a context.

   Example:
   ```python
   with open('file.txt', 'r') as f:
       content = f.read()
   ```

### 20. **What are metaclasses in Python?**
   Metaclasses define the behavior of classes themselves (classes are instances of metaclasses). They can be used to customize class creation, modify class attributes, or enforce design patterns.

   Example:
   ```python
   class Meta(type):
       def __new__(cls, name, bases, dct):
           return super().__new__(cls, name, bases, dct)
   ```


	
	b = minimum_value(a)
	print('min:', b)


 

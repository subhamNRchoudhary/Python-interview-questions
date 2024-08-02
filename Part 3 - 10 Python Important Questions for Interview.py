#sum 1 Third Largest Element

def third_lar(arr):
    if len(arr) < 3:
        return " Least 3 element"
    arr = list(set(arr))
    arr.sort(reverse = True)
    return arr[2]

arr = [66,85,25,1,35,1,2,3]
print(third_lar(arr))

#Sum 2 closest number 

def closest_no(arr , target):
    clo = arr[0]
    for num in arr:
        if abs(num - target) < abs (clo - target):
            clo = num
    return clo

arr = [60,45,35,12,85,78]
target = 2
print(closest_no(arr , target))        

#sum 3 Pairwise maximum

def max_no (arr):
    max_val = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            max_val = max (max_val , arr[i] * arr[j])
    return max_val

arr = [9,56,25,11,0,63,41]

print(max_no(arr))

#sum 4  Binary Representation

def binary_re(n):
    return bin(n)[2:]

n = 10
print(binary_re(n))

#a

def binary_re(b):
    return bin(b)[:2]

b = 10
print(binary_re(b))

#sum 5 Print the Kth Digit

def kth_dig(n,k):
    return int(str(n)[k-1])

n = 123654852
k=6
print(kth_dig(n,k))

#without def function 

a = 123658942525
b = 5
c = int(str(a)[b-1])
print(c)

#sum 6 print doubling the value

a = [2,9,36,5,3,33]
value = 2

for num in a:
    if num == value:
        value *=2


print(value)       


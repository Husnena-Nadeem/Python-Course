#Example no 01
num=[2,7,11,15]
target=9
for i in range(len(num)):
    current_sum=0
    for j in range(i,len(num)):
        current_sum+=num[j]
        if current_sum==target:
            print(f"Subarray from index {i} to {j}:",num[i:j+1])

#Example no 02
num=[3,2,4]
target=6
for i in range(len(num)):
    current_sum=0
    for j in range(i,len(num)):
        current_sum+=num[j]
        if current_sum==target:
            print(f"Subarrat form index {i} to {j}:",num[i:j+1])

#Example no 03
num=[3,3]
for i in range(len(num)):
    current_sum=0
    for j in range(i,len(num)):
        current_sum+=num[j]
        if current_sum==target:
            print(f"subarrat for index {i} to {j}:" ,num[i:j+1])


def is_palindrome(x):
    x_str=str(x)
    return x_str==x_str[::-1]

print(is_palindrome(121))

#Example no 02
def is_palindrome(x):
    x_str=str(x)
    return x_str==x_str[::-1]

print (is_palindrome(-121))

#Example no 0
def is_palindrome(x):
    x_str=str(x)
    return x_str==x_str[::-1]

print (is_palindrome(10))
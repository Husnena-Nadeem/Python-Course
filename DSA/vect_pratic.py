# v=[]
# a1=int(input("Enter the value:"))
# v.append(a1)
# a2=int(input("Enter the value:"))
# v.append(a2)
# a3=int(input("Enter the value:"))
# v.append(a3)
# a4=int(input("Enter the value:"))
# v.append(a4)
# a5=int(input("Enter the value:"))
# v.append(a5)

# print(v)
# print(sum(v))

#maximum and minimum element
v=[1,67,4900,364,-2,-1788]
maximum=max(v)
minimum=min(v)
print("maximum number:",maximum)
print("minimum number:",minimum)

#Reverse an array
v1=[6,7,8,9]
v1.reverse()
print(v1)
#count event numbers and odd numbers
v2=[1,8,9,67,6,2,8,19,10]
for x in v2:
    if x%2==0:
        print(f"Number is even: {x}")
    else:
        print(f"Numbers is odd: {x}")
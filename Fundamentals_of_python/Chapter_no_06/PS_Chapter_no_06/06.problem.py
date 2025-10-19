#Factorial of the Number.

n=int(input("Enter the number"))
product=1
for i in range(1,n+1):
    product=product*i
print(f"Factorial of Number {n}is:\t{product}")
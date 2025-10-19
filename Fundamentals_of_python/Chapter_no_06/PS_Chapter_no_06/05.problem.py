#print the 0,enter number using while loop

n=int(input("Enter the number :"))
i=1
sum=0
while(i<n):
    sum+=i
    i+=1
print(f"sum of this number:",sum)
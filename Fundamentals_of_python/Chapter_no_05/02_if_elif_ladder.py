#If elif else ladder:
a=int(input("Enter your age:\t"))

if(a>=18):
    print("You are above the age of consent")
    print("Good for You:\t")

elif(a<0):
    print("Can't valide Nagative age :") 
elif(a==0):
    print("Can't valide in this age:") 
       
else:
    print("You are blow the age of consent")



print("End of program")  
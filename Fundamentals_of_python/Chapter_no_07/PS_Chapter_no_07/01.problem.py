# 3 number fund grestest number in using function
#using no argument:
def grestNum():
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c=int(input("Enter the number: "))

    if(a>b and a>c):
        print("Grestest number is a:")
    elif(b>a and b>c):
        print("Grestest number is b:")
    else:
        print("Grestest number is c:")

grestNum()  

# this question using arrogument:

def grestNo(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        return "Both are equal"
    
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
print("Grestest number are:",grestNo(a,b,c))
    

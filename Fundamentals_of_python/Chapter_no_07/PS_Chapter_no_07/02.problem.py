"""
write the frogram convert celsius to fahrenheit:
formula to celsius  = c/5 =(f-32)/9.
                    =   c =5*(f-32)/9.
"""
# f=int(input("Enter the temperture in F"))
# c= 5*(f-32)/9

# print(c)


#using no arrogument :
def tem():
    f=int(input("Enter the temperture in F"))
    c= 5*(f-32)/9

    print(c)

tem()    
#using arrogument:
def Tem(f):
    c=5*(f-32)/9
    return c
f=int(input("Enter the temperture in F"))
print(f"Convert celsius to fahrenheit: , = {Tem(f)}°C")
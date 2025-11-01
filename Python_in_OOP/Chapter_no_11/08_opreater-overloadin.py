# class Point:
#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         return self.x + other.x

# p1 = Point(10)
# p2 = Point(20)

# print(p1 + p2)   # Output: 30



class Numbers:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n
    

N1= Numbers(10)
N2= Numbers(20)
result=N1+N2
print(f"sum: {result}")




class Number:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,other):
        sum1=self.a+other.a
        sum2=self.b+other.b
        return Number(sum1,sum2)
    def __sub__(self,other):
        sum1=self.a-other.a
        sum2=self.b-other.b
        return Number(sum1,sum2)
    def __mul__(self,other):
        sum1=self.a*other.a
        sum2=self.b*other.b
        return Number(sum1,sum2)
    def __truediv__(self,other):
        sum1=self.a/other.a
        sum2=self.b/other.b
        return Number(sum1,sum2)
    def __str__(self):  
        return f"a: {self.a}, b: {self.b}"
N1=Number(1,10)
N2=Number(12,90)
print(f"Add the two number:{N1+N2}")
print(f"substract the two number:{N1-N2}")
print(f"Mubtiply the two number:{N1*N2}")
print(f"divide the two number:{N1/N2}")


#1.Tuble is immutable. 
#2.Can't be change.

tuble=(1,3,12,13,16,90,67,3,46)
print(tuble)

print(type(tuble))

a=tuble.count(3)
print(a)


i=tuble.index(12)
print(i)
print(len(tuble))
tuble.sort()
# print(tuble.sort())
# t = (1, 2, 3)              #write the one line 

# for item in t:
#     print(item)
# print(tuble[2])
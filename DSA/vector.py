v=[]
v.append(10)
v.append(20)
v.append(30)
v.append(60)
print("Vector:",v)
#Access elements
print(v[0])
print(v[1])
print(v[2])
#Delete element
v=[1,2,3,7,9,12]
v.pop()
print("delete element",v)
#insert at specific position
v=[16,17]
v.insert(0,15)
print(v)
#Reverse Vector
v.reverse()
print(v)
#Traversal(loop)
employ=[123,456,273,950,678]
for x in v:
    print(x,end=" ")
    
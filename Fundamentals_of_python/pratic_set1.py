#string function
name="Software"
print(name[1:4])

print(name.capitalize())
print(name.find("w"))
print(name.endswith("e"))

#list function
name=[2,34,3,9,23,12,30,10,20,30]
name.append(1000)
print(name)
name.sort()
print(name)
name.reverse()
print(name)
name.remove(2)
print(name)
print(type(name))
name.insert(0,00)
print(name)

#tuble
tub=("name","animal","pepole","things")
print(tub)
print(len(tub))
print(type(tub))
t = tub.index("animal")
print(t)
# 1.List is are mutable .
# 2.canbe change or modifi in realist.
# 3.help store and manage data value under or veriable.

list=["Husnena","apple","bage","tings","School"]

# Function of list
print(len(list))
list.append("Cologe")               #add data attach in end of list
print(list)
print(list[2])
list.insert(0,"Student")             # change the value of  0 index in list
print(list)
                  


list2=[1,36,90,6,8,9,2,4,3]



list2.sort()                            #set the sequence of list
print(list2)

list2.reverse()                         #reverse the list 
print(list2)

value=list2.pop(3)
print(value)
print(list2)

list2.remove(90)                          #remove value 
print(list2)
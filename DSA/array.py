#travelse
arr=[1,2,3,4]
for x in arr:
    print(x)
#reverse
arr=[4,2,7,8,1,2,5]
arr.reverse()
print("reverse:",arr)
#insertion
arr=[2,3,4,6]
arr.append(4)
print("Append",arr)
arr.insert(2,10)
print("insert",arr)
#Deletion
arr=[9,0,8,2,8]
arr.pop()
arr.pop(1)
print(arr)
#searching
arr=[3,5,7]
if 5 in arr:
    print("Found")
    print(arr.index(7))

# reversed
arr=[6,7,8,9]
arr.reverse()
print(arr[::-1])

#sorting
arr=[0,9,8,7]
arr.sort()
print(sorted(arr,reverse=True))



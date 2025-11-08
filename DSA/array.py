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


#Two pointer technique
arr=[1,2,3,4,5]
print(len(arr))
i,j=0,len(arr)-1
while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
print(arr)
#prefix sum
#jb hum index tak ka total chia ho tha ha
arr=[1,2,3,4,5]
prefix=[0]*len(arr)
prefix[0]=arr[0]

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print("Prefix sum Array:",prefix)
#multiple Queries (Fast repeted calculation)
arr=[1,2,3,6,8,11]
prefix=[0]*len(arr)
prefix[0]=arr[0]

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]

queries=[(0,2),(1,4),(2,5)]

for L,R in queries:
    if L ==0:
        print(f"Sum of {L}-{R}:",prefix[R])
    else:
        print(f"Sum of {L}-{R}:",prefix[R]-prefix[L-1])


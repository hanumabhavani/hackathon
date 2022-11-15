#eliminate duplicate number from an array
lst = ['a', 'a', 'b', 'c', 'c', 'd', 'e']
arr=[]
for i in range(len(lst)):
    for j in lst:
        if j not in arr:
            arr.append(j)
print(arr)

def mapArr(arr):
    dict = {}
    for i in range(len(arr)):
        if dict.get(arr[i]):
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
        
    return dict

arr = [1,2,3,4,1,2,2,2,3,3,1,4,1]
result = mapArr(arr)
print(result)
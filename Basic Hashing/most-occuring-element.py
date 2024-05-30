def mostOccuringElement(arr):
    maxElement = -1
    maxValue = 0
    preComputedMap = preComputedMapGenerator(arr)
    for key,val in preComputedMap.items():
        if val > maxValue:
            maxValue = val
            maxElement = key
        else:
            continue
    return maxElement,maxValue
            
    
    
def preComputedMapGenerator(arr):
    dict = {}
    for i in range(len(arr)):
        if dict.get(arr[i]):
            dict[arr[i]] += 1
        else: 
            dict[arr[i]] = 1
    return dict

arr = [1,2,3,4,1,2,2,2,3,3,1,4,1,1] 
print(mostOccuringElement(arr))
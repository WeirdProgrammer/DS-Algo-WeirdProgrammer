arr = [1,3,5,7,9] 

def do(arr):
    min = arr[:-1]
    # print(min)
    max = arr[1:]
    # print(max)
    
    # minSum = [x + x for x in min]
    minSum = getSum(min)
    print(min)
    print(minSum)
    print('#############################')
    maxSum = getSum(max)
    print(max)
    print(maxSum)

def getSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


do(arr)
class Combo:
    def __init__(self):
        pass
    
    def KthMax(self, arr, k):
        m = max(arr)
        if k == 1:
            return m
        else:
            print('1 more rec')
        
        arr = [x for x in arr if x != m]
        
        return self.KthMax(arr, k-1)
    
    def Stones(self, arr):
        print(arr)
        if len(arr) == 1:
            return arr
        m1 = max(arr)
        arr = [x for x in arr if x != m1]
        m2 = max(arr)
        arr = [x for x in arr if x != m2]
        res = m1 - m2
        
        arr.append(abs(res))
        
        return self.Stones(arr)
        
        
        
if __name__ == '__main__':
    com = Combo()
    arr = [2,7,4,1,8,1]
    com.Stones(arr)
    # arr = [2,4,1,5,6,0]
    
    # res = com.KthMax(arr=arr, k=2)
    # print(res)
    
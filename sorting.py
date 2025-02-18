class Sort:
    def __init__(self, arr) -> None:
        self.arr = arr
        
    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            j = i
            for j in range(j, n):
                if self.arr[i] > self.arr[j]:
                    self.arr[i] ,self.arr[j] =self.arr[j] , self.arr[i]
                # if self.arr[i] < self.arr[j]:
                #     self.arr[i] ,self.arr[j] =self.arr[j] , self.arr[i]
                    
        print(self.arr)
        
    def quick_sort(self ,arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[-1]
        
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
        
if __name__ == '__main__':
    arr = [ 0, 3, 4 ,3 , 6 , 11 ,8 , -1]
    sort = Sort(arr)
    
    sort.bubble_sort()
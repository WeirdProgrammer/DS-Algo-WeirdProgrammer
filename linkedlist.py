class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next
        
        
        
class LinkedList:
    def __init__(self) -> None:
        pass
    
    def addFirst(self, val):
        pass
    
    def addEnd(self, val):
        pass
    
    def update(self, val):
        pass
    
    def delete(self, val):
        pass
    
    def mergeTwoLists(self, list1, list2):
        dummy = Node()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
            
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
            
        return dummy
    
    def display(self, node):
        curr = node
        while curr:
            print(curr.val)
            curr = curr.next
            
if __name__ == '__main__':
    head = Node(1)
    a = Node(2)
    b = Node(3)
    
    head.next = a
    a.next = b
    
    
    head1 = Node(1)
    a1 = Node(4)
    b1 = Node(11)
    
    head1.next = a1
    a1.next = b1
    
    linked = LinkedList()
    # linked.display(head)
    merged = linked.mergeTwoLists(head, head1)
    linked.display(merged)
    
    
    
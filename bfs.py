class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
        
        
class Tree:
    def __init__(self) -> None:
        pass
    
    def display(self, node):
        if node is None:
            return
        
        print(node.val)
        self.display(node.right)
        self.display(node.left)
        
        
    def maxTreeDepth(self, root):
        if not root: return 0
        left = self.maxTreeDepth(root.left)
        right = self.maxTreeDepth(root.right)
        
        return 1 + max(left, right)
        
        
if __name__ == '__main__':
    root = Node(1)
    a = Node(2)
    b = Node(3)
    c = Node(4)
    d = Node(5)
    
    root.right = a
    root.left = b
    a.right = c
    a.left = d
    
    tree = Tree()
    tree.display(root)
    
    print('max depth : ',tree.maxTreeDepth(root))
    
        
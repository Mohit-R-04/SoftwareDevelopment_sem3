class node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

class bst:
    def __init__(self):
        self.head = None
        
    def insert(self,val,current=None):
        try:
            
            if self.head == None:
                self.head = node(val)
                current = self.head
            else:
                if current is None:
                    current = self.head
                if current.val > val:
                    if current.l is None:
                        current.l = node(val)
                    else:
                        self.insert(val,current=current.l)
                else:
                    if current.r is None:
                        current.r = node(val)
                    else:
                        self.insert(val,current=current.r)
        except Exception as E:
            print("cant insert given val")
            
    def traversal(self,Type,node=None):
        if node is None:
            node = self.head
        if Type == "inorder":
            return self._inorder_traversal(node)
        elif Type == "preorder":
            return self._preorder_traversal(node)
        elif Type == "postorder":
            return self._postorder_traversal(node)
        
    def _inorder_traversal(self,node):
        result = []
        if node.l:
            result += self._inorder_traversal(node.l)
        result += [node.val]
        if node.r:
            result += self._inorder_traversal(node.r)
            
        return result
            
    def _preorder_traversal(self,node):
        result = []
        result += [node.val]
        if node.l:
            result += self._inorder_traversal(node.l)
        if node.r:
            result += self._inorder_traversal(node.r)
            
        return result
    
    def _postorder_traversal(self,node):
        result = []
        if node.l:
            result += self._inorder_traversal(node.l)
        if node.r:
            result += self._inorder_traversal(node.r)
        result += [node.val]
        
        return result
    
    
tree = bst()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.traversal(Type="inorder"))    # [5, 10, 15]
print(tree.traversal(Type="preorder"))   # [10, 5, 15]
print(tree.traversal(Type="postorder"))  # [5, 15, 10]

    
    
    
    
    
    
    
    
    
    
    
    

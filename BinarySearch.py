#Binary Search Algorithm
# a tree where each node is a value greater than all of its left child nodes
# and less than all of its right child nodes

class BSAlgo:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
        return
        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
        return
        self.right = BSTNode(val)

        #functions to find the smallest and largest values

    def get_min(self):
        current = self
        while current.left is not None:
         current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    # function to order incase of a deletion
    #function to order 

#call the functions
    
def main ():
    nums = [11, 6, 8, 9, 21, 11, 3, 15, 14, 24, 18]
    bst = BSAlgo()
    for num in nums:
        bst.insert(num)
    
    print(bst)
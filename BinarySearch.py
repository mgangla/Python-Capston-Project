#Binary Search Algorithm
# a tree where each node is a value greater than all of its left child nodes
# and less than all of its right child nodes

class BSAlgo:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    #A new key is always inserted at the leaf by maintaining the property of the binary search tree. 
    #We start searching for a key from the root until we hit a leaf node. 
    #Once a leaf node is found, the new node is added as a child of the leaf node

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
    # 3scenarios

    #1.Deleting a single child node is also simple in BST. 
    #Copy the child to the node and delete the node. 

    #2. Delete a Leaf Node in BST
    #3.Delete a Node with Both Children in BST
    # Here we have to delete the node is such a way,
    # that the resulting tree follows the properties of a BST.  

    #we need to find the inorder successor of the node. 
    #Copy contents of the inorder successor to the node, and delete the inorder successor.

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
    

    #function to order## Traversals
    #Inorder, Preorder, Post Order
    #Helps print out the tree in a readable format. 
    #The inorder method print’s the values in the tree in the order of their keys.

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)

        if self.val is not None:
            vals.append(self.val)

        if self.right is not None:
            self.right.inorder(vals)

        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)

        if self.left is not None:
            self.left.preorder(vals)

        if self.right is not None:
            self.right.preorder(vals)

        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)

        if self.right is not None:
            self.right.postorder(vals)

        if self.val is not None:
            vals.append(self.val)
        return vals
    
    #function to check if a value exists returns true or false
    
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)



#call the functions
    
def main ():
    nums = [11, 6, 8, 9, 20, 4, 3, 15, 14, 24, 18]
    bst = BSAlgo()
    for num in nums:
        bst.insert(num)
        print("preorder:")
        print(bst.preorder())
        print("#")

        print("postorder:")
        print(bst.postorder())
        print("#")

        print("inorder:")
        print(bst.inorder())
        print("#")

        #to search for a key value

    search_key = 24
    search_result = bst.exists(search_key)

    if search_result:
        print(f"Key {search_key} found in the BST.")
    else:
        print(f"Key {search_key} not found in the BST.")


    nums = [2, 6, 20]
    print("deleting " + str(nums))

    for num in nums:
        bst.delete(num)
        print("#")

        print(bst.exists(4))
        print("2 exists:")
        print(bst.exists(2))
        print("12 exists:")
        print(bst.exists(12))
        print("18 exists:")
        print(bst.exists(18))
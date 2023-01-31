class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# a function to do inorder tree traversal 
def printinorder(root):
    if root:
        # first recur on left chid
        printinorder(root.left)
        
        #then print  the data of node
        print(root.val)
        
        # now recure on right child
        printinorder(root.right)

def printpreorder(root):
    if root:
        
        #then print the data of node
        print(root.val)
        
        #first recure on left child
        printpreorder(root.left)
        
        #now recure on right child
        printpreorder(root.right)
        
def printpostorder(root):
    if root:
        #first recure on left child
        printpreorder(root.left)
        
        #now recure on right child
        printpreorder(root.right)
        
        #then print the data of node
        print(root.val)

# driver code
#if __name__ == "__main__":
root = Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left = Node(4)
root.left.right =Node(5)
    
# Function call
print('\nInorder traversal of binary tree is : ')
printinorder(root)
print('\nPreorder traversal of binary tree is : ')
printpreorder(root)
print('\nPostorder traversal of binary tree is : ')
printpostorder(root)




    

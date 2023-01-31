class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def printpreorder(root):
    if root:
        print(root.val)
        printpreorder(root.left)
        printpreorder(root.right)


def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val)


root= Node(1)
root.left= Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

print(" \n Inorder Traversal of the binary tree : ")
printInorder(root)
print(" \n Preorder Traversal of the binary tree : ")
printpreorder(root)
print(" \n Postorder Traversal of the binary tree : ")
printpostorder(root)
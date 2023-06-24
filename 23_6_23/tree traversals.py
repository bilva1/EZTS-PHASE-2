class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.data,end=" ")
        printinorder(root.right)
def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.data,end=" ")
def printpreorder(root):
    if root:
        print(root.data,end=" ")
        printpreorder(root.left)
        printpreorder(root.right)
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("Preorder:")
printpreorder(root)
print()
print("Postorder:")
printpostorder(root)
print()
print("inorder:")
printinorder(root)



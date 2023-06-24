#single linkedlist using dynamic input
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def add(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        temp=self.head
        while temp:
            if temp.next!=None:
                print(temp.data,"->",end=' ')
            else:
                print(temp.data,end=" ")
            temp=temp.next
llist=LinkedList()
n=int(input("How many elements would you like to add?"))
for i in range(n):
      data=int(input("Element:"))
      llist.add(data)
print("The linked list:",end=" ")
llist.display()
            

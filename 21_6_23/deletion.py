class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while  temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
obj=Linkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before deletion")
obj.display()
obj.delete_begin()
print("\nAfter deleting 1st element")
obj.display()
obj.delete_end()
print("\nAfter deleting last element")
obj.display()
obj.delete_pos(3)
print("\nAfter deleting at 3rd position")
obj.display()

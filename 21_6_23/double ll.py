class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty!")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"<-->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
obj=dll()
n1=Node(10)
obj.head=n1
n2=Node(11)
n1.next=n2
n2.prev=n1
n3=Node(20)
n2.next=n3
n3.prev=n2
n4=Node(45)
n3.next=n4
n4.prev=n3
obj.display()

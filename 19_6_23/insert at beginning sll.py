class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end="")
                else:
                    print(temp.data,end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
print("\nBefore inserting 100:")
obj.display()
print("\nafter inserting 100:")
obj.insert_beginning(100)
obj.display()
print("\nafter inserting 200:")
obj.insert_beginning(200)
obj.display()
            

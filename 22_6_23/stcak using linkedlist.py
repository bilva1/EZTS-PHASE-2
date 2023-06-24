class Node:
    def __init__(self,data):
        self.data=data
        self.head=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        temp=self.head
        if temp==None:
            print("cannot pop!")
            return
        else:
            self.head=temp.next
            temp.next=None
            print(f"popped element={temp.data}")
    def display(self):
        temp=self.head
        if temp is None:
            print("Sorry! Your stack is empty.")
        else:
            print("temp.data","->",end=" ")
            temp=temp.next
obj=stack()
while True:
    print("push <value>")
    print("pop")
    print("Quit")
    m=input("push what? ").split()
    d=m[0].strip().lower()
    v=int(m[1])
    if d=="push":
        obj.push(v)
    elif d=="pop":
        obj.pop()
    elif d=="display":
        obj.display()
    elif d=="quit":
        break
    else:
        print("please enter correctly!")
    
    
            

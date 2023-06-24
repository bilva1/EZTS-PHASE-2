class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            r=self.head.data
            self.head.next=self.head
            return r
obj=queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")
    m=input("op value:").split()
    p=int(m[1])
    m[0].strip().lower()
    if m[0]=="enqueue":
        obj.enqueue(p)
    elif m[0]=="dequeue":
        obj.dequeue()
    elif m[0]=="quit":
        break

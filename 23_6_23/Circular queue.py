class CircularQueue():
    def __init__(self,size):
        self.size=size
        #None is generally used for actiavating
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condition if queue is full
        if ((self.rear+1)%self.size==self.front):
            print("Queue is full\n")
        #condition for empty queue
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
            #condition for empty queue
            print("Queue is Empty\n")
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #condition for empty queue
        if(self.front==-1):
            print("Queue is empty")
        elif(self.rear>=self.front):
            print("Elements in the circular queue",end=" ")
            for i in range(self.front,self.size+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("Elements:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if ((self.rear+1)%self.size==self.front):
            print("Queue is Full")
obj=CircularQueue(5)
obj.enqueue(14)
obj.enqueue(22)
obj.enqueue(13)
obj.enqueue(-6)
obj.display()
print("Deleted Value:",obj.dequeue())
print("Deleted Value:",obj.dequeue())
obj.display()
obj.enqueue(9)
obj.enqueue(20)
obj.enqueue(5)
obj.display()
#it want be inserted bsc queue full            
obj.enqueue(100)

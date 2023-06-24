stack=[]
estack=[]
ostack=[]
def push(x):
    stack.append(x)
    if x%2==0:
        estack.append(x)
        
    else:
        ostack.append(x)
def pop():
    stack.pop()
    pop_what=int(input("Enter 1 to pop from even list and 0 for odd list"))
    if pop_what==1:
        if not ostack:
            print("empty stack")
        else:
            estack.pop()
    elif pop_what==0:
        if not estack:
            print("empty stack")
        else:
            ostack.pop()
    
def show(m):
    if m==1:
        print(estack)
    elif m==0:
        print(ostack)
size=int(input("size:"))    
for _ in range(size):
    while True:
        n=int(input("value:"))
        choice=input("operations 1.push 2.pop 3.show 4.quit:")
        
        if choice=='1':
            push(n)
        elif choice=='2':
            pop()
        elif choice=='3':
            m=int(input(" enter 1 for evenlist and 0 for odd list and 2 for the combined stack:"))
            show(m)
        elif choice=='4':
            break
        else:
            print("Invalid input.Try again!")

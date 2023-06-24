#stack implementation using arrays
stack=[]
def push():
    element=int(input("Element to push:"))
    stack.append(element)
def pop():
    """if not stack:
        return
    else:
        rem=stack.pop()
        print(f"removed element:{rem}")
    or"""
    if len(stack)==Null:
        print("stack empty!")
    else:
        print(f"top={stack[-1]}")
def top():
    if not stack:
        print("oops! Stack is empty")
    else:
        top=stack.pop()
        print(f"top={top}")
def display():
    if stack==None:
        print("Stack is empty!")
    else:
        print(stack)
while True:
    print("""select operation:
          \n1.Push\n 2.Pop\n 3.Quit\n 4.display\n 5.top\n""")
    choice=int(input("choice:"))
    if choice==1:
        push()
        
    elif choice==2:
        pop()
    elif choice==3:
        break
    elif choice==4:
        display()
    elif choice==5:
        top()
    else:
        print("please enter again")
    

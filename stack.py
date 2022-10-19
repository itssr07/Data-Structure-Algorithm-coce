stack=[]
def push():
    if len(stack)==n:
        print("list is full!")
    else:
        element=input("Enter the element")
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("stack is empty!")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)

n=int(input("Limit of stack"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct operation!")
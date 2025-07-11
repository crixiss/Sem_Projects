n=input("Enter the number of elements: ")
lst = []
for i in range(int(n)):
    num = int(input("Enter number: "))
    lst.append(num)
    
while True:
    print("\n1.Push\n2.Pop\n3.Enqueue\n4.Dequeue\n5.Exit")
    ch = int(input("Choose: "))
    if ch == 1:
        val = input("Push value: ")
        lst.append(val)
        print("Stack after push:", lst)
    elif ch == 2:
        if lst: print("Popped:", lst.pop())
        else: print("Empty Stack")
        print("Stack after pop:", lst)
    elif ch == 3:
        val = input("Enqueue value: ")
        lst.append(val)
        print("Queue after enqueue:", lst)
    elif ch == 4:
        if lst: print("Dequeued:", lst.pop(0))
        else: print("Empty Queue")
        print("Queue after dequeue:", lst)
    elif ch == 5:
        break

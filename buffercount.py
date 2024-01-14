n = int(input("Enter buffer size: "))
buffer = 0
print('''1: producer
2: consumer
3: exit''')
a = int(input("Enter choice: "))
while a == 1 or a == 2:
    if a == 1:
        if buffer >= n:
            print("Buffer full")
        else:
            buffer += 1
            print("Producer produces item", buffer)
    else:
        if buffer <= 0:
            print("Buffer empty")
        else:
            print("Consumer consumes item", buffer)
            buffer -= 1
    print("Buffer count:", buffer)
    a = int(input("Enter choice: "))
print("Exit")

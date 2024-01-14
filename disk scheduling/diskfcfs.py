def fcfs(arr, head):
    n = len(arr)
    total = 0
    order = [head] # to store the order of disk requests
    for i in range(n):
        distance = abs(arr[i] - head)
        total += distance
        head = arr[i]
        order.append(head)
    return total, order
arr = [int(x) for x in input("Enter the disk requests: ").split()]
head = int(input("Enter the starting head position: "))
total_distance, request_order = fcfs(arr, head)
print("Total head movements: ", total_distance)
print("Request order: ", request_order)

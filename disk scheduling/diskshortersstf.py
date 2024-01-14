def sstf(arr, head):
    total, order = 0, [head]
    while arr:
        i = min(range(len(arr)), key=lambda x: abs(arr[x]-head))
        total += abs(head - arr[i])
        head = arr.pop(i)
        order.append(head)
    return total, order
arr = list(map(int, input("Enter the disk requests: ").split()))
head = int(input("Enter the starting head position: "))
total_distance, request_order = sstf(arr, head)
print("Total head movements: ", total_distance)
print("Request order: ", request_order)
 
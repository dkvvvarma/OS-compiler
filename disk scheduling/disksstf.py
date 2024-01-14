def sstf(arr, head):
    n = len(arr)
    total = 0
    order = [head] 
    while len(arr) > 0:
        min_dist = float('inf')
        min_index = -1
        for i in range(len(arr)):
            distance = abs(arr[i] - head)
            if distance < min_dist:
                min_dist = distance
                min_index = i
        total += min_dist
        head = arr[min_index]
        order.append(head)
        arr.pop(min_index)
    return total, order
arr = [int(x) for x in input("Enter the disk requests: ").split()]
head = int(input("Enter the starting head position: "))
total_distance, request_order = sstf(arr, head)
print("Total head movements: ", total_distance)
print("Request order: ", request_order)

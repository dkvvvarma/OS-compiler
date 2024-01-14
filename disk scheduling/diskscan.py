def scan(arr, head):
    total = 0
    order = []
    n = len(arr)
    left_arr = [x for x in arr if x < head]
    right_arr = [x for x in arr if x >= head]
    left_arr.sort(reverse=True)
    right_arr.sort()
    order += left_arr
    order += right_arr
    for i in range(len(order)):
        total += abs(head - order[i])
        head = order[i]
    return total, order
arr = [int(x) for x in input("Enter the disk requests: ").split()]
head = int(input("Enter the starting head position: "))
total_distance, request_order = scan(arr, head)
print("Total head movements: ", total_distance)
print("Request order: ", request_order)

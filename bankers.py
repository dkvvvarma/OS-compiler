
import copy

def bankers_algorithm(n, m, available, max_req, allocation):
    need = [[max_req[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    running = [True] * n
    safe_sequence = []
    work = copy.deepcopy(available)
    while any(running):
 ..       safe = False
        for i in range(n):
            if running[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + allocation[i][j] for j in range(m)]
                running[i] = False
                safe_sequence.append(i)
                safe = True
        if not safe:
            return (False, [])
    return (True, safe_sequence)

# User input
n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources: "))

available = list(map(int, input("Enter the available resources: ").split()))

max_req = []
for i in range(n):
    max_req.append(list(map(int, input(f"Enter the maximum resource request for process {i}: ").split())))

allocation = []
for i in range(n):
    allocation.append(list(map(int, input(f"Enter the allocated resources for process {i}: ").split())))

result, sequence = bankers_algorithm(n, m, available, max_req, allocation)
if result:
    print("Safe sequence: ", sequence)
else:
    print("The system is in an unsafe state.")
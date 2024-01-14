#FIFO
frames = int(input("Enter the capacity of the memory: "))
processList = list(map(int, input("Enter the process list: ").split()))
s = []
pageFaults = 0
for i in processList:
    if i not in s:
        if(len(s) == frames):
            s.pop(0)  # remove the first element
            s.append(i)  # add new element at the end
        else:
            s.append(i)
        pageFaults +=1
print("Number of Page Faults: {}".format(pageFaults))
#LRU
frames = int(input("Enter the capacity of the memory: "))
processList = list(map(int, input("Enter the process list: ").split()))
s = []
pageFaults = 0
for i in processList:
    if i not in s:
        if(len(s) == frames):
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pageFaults +=1
    else:
        s.remove(i)
        s.append(i)
print("Number of Page Faults: {}".format(pageFaults))
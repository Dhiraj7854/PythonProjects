n = int(input("Enter number of elements: "))
ele = input("Enter space separated values: ")
lst = []
lst = list(map(int, ele.split()))
count = 0
for i in range(n):
    min = i
    for j in range(i+1,n):
        if lst[j] < lst[min]:
            min = j
    
    lst[min], lst[i] = lst[i], lst[min]
    if min != i:
        count += 1
    
print(f"Sorted list: {lst}")
print(count)
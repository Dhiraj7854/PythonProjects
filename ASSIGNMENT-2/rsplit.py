text = input("Enter your text: ")
delm = input("Enter parameter: ")
n = int(input("Enter the times of splitting: "))

lst = []
prev_j = len(text)

count = 0
for i in range(len(text) - 1, 0, -1):
    if text[i] == delm:
        j = i
        lst.append(text[j + 1:prev_j])
        prev_j = j
        count += 1
        if count == n:
            break
lst.append(text[0:prev_j])
print(lst)
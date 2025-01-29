text = input("Enter your text: ")
old = input("Enter old word: ")
new = input("Enter new word: ")
count = int(input("Enter the number of replacements: "))

lst2 = []
i = 0
j = 0
while i<len(text):
    if text[i:i+len(old)] == old and (j == 0 or j<count):
        lst2.append(new)
        i += len(old)
        j += 1
    else:
        lst2.append(text[i])
        i += 1
updated = ''.join(lst2)
print(updated)
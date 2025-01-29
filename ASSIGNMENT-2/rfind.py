text = input("Enter your text: ")
print("Length of text",len(text))
sub_text = input("Enter the sub-string to search for: ")

print("Keep start as 0 and end as text length for searching in whole string")

start = int(input("Enter starting position: "))
end = int(input("Enter your end position: "))
pos = -1
for i in range(start,end+1):
    if (text[i:i+len(sub_text)] == sub_text):
        pos = i

if (pos == -1):
    print(-1)
else:
    print("Last Occurrence:",pos)
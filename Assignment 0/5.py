num = int(input("ENter any number: "))
n = int(input("Enter the  number of tables: "))

"""PRINTING TABLES USING LOOP"""

for i in range(1,n+1):
    print(f"{num} * {i} = {num*i}")

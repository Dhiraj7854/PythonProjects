test_cases = int(input("Enter number of testcases: "))
N = int(input("Enter boxes: "))
X = int(input("position of coin: "))
S = int(input("Enter number of swaps: "))
for i in range(S):
    a = int(input())
    b = int(input())
    if X == a:
        X = b
    elif X == b:
        X = a
print(f"Final Position of coin: {X}")
#PROGRAM TO REVERSE A NUMBER
n = int(input("Enter a number: "))

#CONVERTING TO STRING
string = str(n)

#USING string[::-1] TO REVERSE AND PRINT CONVERTING TO int AGAIN
print(f"Reverse number: {int(string[::-1])}")


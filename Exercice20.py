# Input the first integer
A = int(input("Enter the first integer: "))

# Input the second integer
B = int(input("Enter the second integer: "))

# Input the operator
operateur = input("Enter the operator (+, -, *, /): ")

# Determine the result based on the operator
if operateur == '+':
    resultat = A + B
elif operateur == '-':
    resultat = A - B
elif operateur == '*':
    resultat = A * B
elif operateur == '/':
    if B != 0:
        resultat = A / B
    else:
        print("Error: Division by zero.")
        resultat = "Undefined"
else:
    print("Invalid operator.")
    resultat = "Undefined"

# the result
print("The result of", A, operateur, B, "is:", resultat)

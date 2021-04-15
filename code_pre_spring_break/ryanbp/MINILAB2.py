
num1 = int(input("Enter Any Number: "))
num2 = int(input("Enter Any Number: "))

# INPUT
print("Which operation would you like to perform?")
ryan = input("Enter desired operation +  -  *  /  : ")

# PROCEDURE
result = 0
if ryan == '+':
    result = num1 + num2
elif ryan == '-':
    result = num1 - num2
elif ryan == '*':
    result = num1 * num2
elif ryan == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")
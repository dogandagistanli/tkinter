def control(num1, num2):
    return mirror(num1) == num2

def mirror(n1):
    n2 = (n1 % 10) * 10 + (n1 // 10)
    return n2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
is_mirror = control(num1, num2)

while is_mirror:
    print("%d and %d are mirrors." % (num1, num2))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    is_mirror = control(num1, num2)

print("%d and %d are not mirrors." % (num1, num2))

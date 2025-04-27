num = int(input("Enter a number: "))
sum = 0
def addDigits(num, sum):
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    print("Sum of two digits:" , sum)

addDigits(num, sum)


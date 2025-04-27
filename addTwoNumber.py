def addTwoNumber(a, b):
    c = [0] * len(a)
    num1 = 0
    num2 = 0

    for i in range(len(a) - 1, -1, -1):
        num1 = (num1 * 10) + a[i]
    print(num1)

    for j in range(len(b) - 1, -1, -1):
        num2 = (num2 * 10) + b[j]
    print(num2)


    num3 = num1 + num2
    print(num3)   


    for k in range(0, len(a)):
        r = num3 % 10
        c[k] = r
        num3 = num3 // 10

    print(c)

a = [2, 4, 3]
b = [5, 6, 4]

addTwoNumber(a, b)
        


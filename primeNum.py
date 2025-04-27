def primeNum(num):
    sum = 0
    for i in  range(1, num):
        if num % i == 0:
            sum+= 1
        
    if sum >= 2:
        for i in  range(1, num):
            if num % i == 0:
                
                print(i)
        print(num, " is a prime number")
    else:
        print(num, "is not a prime number")

num = int(input("Enter a number: "))
primeNum(num)

sum = 0
count = 0
while True:
    try:
        n= input("Enter a number: ")
        num = float(n)
        print(num)
        sum += num
        count += 1
    except:
        if n == "done":
            print(int(sum), count, sum/count)
            break
        else:
            print("Invalid input")
    
    
    
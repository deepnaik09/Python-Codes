largest = None
smallest = None
while True:
    try:
        n = input("Enter a number: ")
        num = int(n)
    except:
        if n == "done":
            print("Maximum is", largest)
            print("Minimum is", smallest)
            break
        else:
            print("Invalid input")
    if largest == None:
        largest = num
    elif num > largest:
        largest = num
    elif smallest == None:
        smallest = num
    elif num < smallest:
        smallest = num
    else:
        continue
            
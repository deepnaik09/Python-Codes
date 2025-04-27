total = 0
count = 0
while True:
    n = input("Enter a number: ")
    if n == 'done': break
    value = float(n)
    total = total + value
    count += 1
avg = total/count
print("Average:", avg) 
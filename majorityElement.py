list1 =  [3, 3, 4]
lastCount = 0
max = 0

for i in list1:
    counter = 0
    for j in list1:
        print(i, j)
        currentNum = i
        if currentNum == j:
            counter += 1
    if counter>lastCount:
        print("Comparison: ", counter, lastCount)
        lastCount = counter
        max = i
print(max)


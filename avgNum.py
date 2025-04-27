count = 0
sum = 0
print("Before: ", count)
for value in [9, 41, 12, 3,  74, 15]:
    count +=1
    sum +=value
    print(count, sum)
print(count, sum, sum/count)
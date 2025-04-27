total = 0
count = 0
numList = list()
while True:
    n = input("Enter a number: ")
    if n == 'done': break
    value = float(n)
    numList.append(value)
avg = sum(numList)/len(numList)
print('Average: ', avg)

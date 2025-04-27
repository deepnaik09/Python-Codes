file = open("text.txt")
count = 0
for cheese in file:
    count += 1
print(count, "lines")
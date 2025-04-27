def strToInt(text):
    outputNum = 0
    for char in text:
        for i in range(10):
            if str(i) == char:
                outputNum = (outputNum * 10) + i
    return outputNum
    

text = input("Enter a Number:")
output = strToInt(text)
print(output)



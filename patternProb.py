current_char = ord('A')
n = int(input("Enter a number: "))
for i in range(0, n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print(chr(current_char).upper(), end = ' ')
            
        else:
            print(chr(current_char).lower(), end = ' ')
        current_char += 1
    print()

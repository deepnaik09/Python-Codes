n = int(input("Enter Number of  elements: "))
arr  = []
for i in range(n):
    m = input()
    if m.isdigit() or (m[0] == '-' and m[1:].isdigit()):
        arr.append(int(m))
    else:
        arr.append(m)
print(arr)
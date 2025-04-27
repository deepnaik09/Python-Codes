dict1 = {}
arr = ['chuck', 'red', 'chuck', 'red', 'red', 'chuck', 'chuck', 'chuck', 'red', 'chuck', 'red']
for i in arr:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)

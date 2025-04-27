dict1 = {}
arr = ['chuck', 'red', 'chuck', 'red', 'red', 'chuck', 'chuck', 'chuck', 'red', 'chuck', 'red']
for name in arr:
    dict1[name] = dict1.get(name, 0) + 1
print(dict1)
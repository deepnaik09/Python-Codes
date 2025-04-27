import re
n = input()
print(re.search(r"^[-+]?\d*\.\d+$", n))
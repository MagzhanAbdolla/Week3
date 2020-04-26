n = int(input())
Plus = 0.0
i = 1
for i in range(1, n + 1):
    s = 1.0 / (i**2)
    Plus += s
    i = i + 1
print(Plus)

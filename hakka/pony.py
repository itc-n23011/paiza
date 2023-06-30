def pony(n, m):
    return "OK" if n == m else "NG"


n, m = input().split()

result = pony(n, m)
print(result)

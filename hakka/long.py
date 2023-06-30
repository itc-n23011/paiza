def A(N):
    return "lucky" if N % 7 == 0 else "unlucky"


N = int(input())

result = A(N)
print(result)

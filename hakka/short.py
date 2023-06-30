def A(num, moji):
    return "\n".join([moji] * num)


num, moji = int(input()), input()

result = A(num, moji)
print(result)

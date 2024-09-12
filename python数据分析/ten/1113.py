def digui(n):
    sum = 0
    if n < = 0:
        return 1
    else:
        return n * digui(n - 1)

print(digui(5))
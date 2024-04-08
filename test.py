def f(x):
    return 5*(x-1)

def find(a1, n):
    an = a1
    for i in range(1, n + 1):
        if i == 1:
            an == 1
        else:
            an += f(i)
    return an

print(find(1, 2))
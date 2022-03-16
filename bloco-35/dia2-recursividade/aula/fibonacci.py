acc = 0
initial = 1
index = 0

while index != 11:
    acc = acc + initial
    initial = initial + acc
    index += 1
    print(acc, initial)


def fibo(n):
    sequence = [0, 1]
    if n >= 2:
        for x in range(2, n + 1):
            next = sequence[-1] + sequence[-2]
            sequence.append(next)
    return sequence[n]


print(fibo(9))


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

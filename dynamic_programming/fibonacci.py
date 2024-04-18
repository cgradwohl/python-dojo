def fib(n):
    if n < 1:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_memo(n, dp={}):
    if n < 1:
        return 0

    if n == 1:
        return 1

    if n in dp:
        return dp[n]

    dp[n] = fib_memo(n - 1, dp) + fib_memo(n - 2, dp)

    return dp[n]


def fib_fast(n):
    if n <= 0:
        return 0
    if n > 0 and n <= 2:
        return 1

    f1, f2 = 1, 1
    for _ in range(3, n + 1, 1):
        temp = f1
        f1 = f2
        f2 = temp + f1

    return f2


print("fib fast: ", fib_fast(37))
print("fib memo: ", fib_memo(37))
print("fib: ", fib(37))

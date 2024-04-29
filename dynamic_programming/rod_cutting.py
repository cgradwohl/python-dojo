def dfs(P, n, memo={}):
    if n == 0:
        return 0

    if n in memo:
        return memo[n]

    revenue = -float('inf')
    for length in range(1, len(P)):
        if n - length < 0:
            continue

        price = dfs(P, n - length, memo)
        revenue = max(P[length] + price, revenue)

    memo[n] = revenue
    return revenue


P = [0, 1, 4, 4, 5]
n = 12
print(dfs(P, n))


def dp(P, n):
    memo = [-float('inf')] * (n + 1)

    # base case
    memo[0] = 0

    for i in range(1, n + 1):
        for length in range(1, len(P)):
            if i-length >= 0:
                memo[i] = max(memo[i-length] + P[length], memo[i])

    return memo[n]


print(dp(P, n))

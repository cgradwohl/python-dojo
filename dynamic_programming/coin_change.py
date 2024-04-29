def dfs(coins, amount, memo={}):
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    if amount in memo:
        return memo[amount]
    minCount = float('inf')
    for coin in coins:
        if amount - coin < 0:
            continue

        count = dfs(coins, amount - coin)
        minCount = min(minCount, count + 1)

    memo[amount] = minCount
    return -1 if minCount == float('inf') else minCount


coins = [1, 3, 4, 5]
amount = 100

print(dfs(coins, amount))

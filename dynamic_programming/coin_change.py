def brute_force(coins, amount):
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    minCount = float('inf')
    for coin in coins:
        count = brute_force(coins, amount - coin)
        if count == -1:
            continue
        minCount = min(minCount, count + 1)

    return -1 if minCount == float('inf') else minCount

def greedy_brute_force(coins, amount):
    results = []
    coins = sorted(coins, reverse=True)
    for i in range(len(coins)):
        coin = coins[i]
        if coin > amount:
            continue
        result = [coin]
        _amount = amount - coin

        ptr = i
        while ptr < len(coins):
            if coins[ptr] <= _amount:
                _amount -= coins[ptr]
                result.append(coins[ptr])
            else:
                ptr += 1

        results.append(len(result))
    return min(results)


print(greedy_brute_force([5, 2, 1], 11))

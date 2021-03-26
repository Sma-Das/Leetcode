def coinChange(coins: list[int], amount: int) -> int:

    def bestChange(coins, amount, count=0):

        if amount == 0:
            return count

        min_val = float('inf')

        for coin in coins:
            if amount - coin < 0:
                continue
            possible = bestChange(coins, amount-coin, count+1)
            if possible:
                min_val = min(min_val, possible)
        return min_val if min_val != float('inf') else -1

    return bestChange(tuple(coins), amount)

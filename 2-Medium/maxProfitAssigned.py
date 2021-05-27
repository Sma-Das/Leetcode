def maxProfitAssigned(difficulty, profit, worker):
    return sum(max(p for d, p in zip(difficulty, profit) if d <= work) for work in worker)

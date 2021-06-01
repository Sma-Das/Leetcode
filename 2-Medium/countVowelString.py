def countVowelString(n: int):
    dp = [1] * 5
       for _ in range(n):
            dp = accumulate(dp)
        return list(dp)[-1]


if __name__ == '__main__':
    countVowelString(33)

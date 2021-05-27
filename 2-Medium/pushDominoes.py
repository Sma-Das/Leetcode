def pushDominoes(dominoes: str):
    while True:
        res = list(dominoes)
        for r in range((length := len(dominoes))-1):
            if dominoes[r] == "R" and res[r+1] == ".":
                res[r+1] = "R."
        for l in range(1, length):
            if res[l] == "L":
                if (v := res[l-1]) == ".":
                    res[l-1] = "L"
                elif v == "R.":
                    res[l-1] = "."
        res = [v if v != "R." else "R" for v in res]
        if (doms := "".join(res)) != dominoes:
            dominoes = doms
        else:
            break
    return dominoes


if __name__ == '__main__':
    print(pushDominoes(".L.R...LR..L.."))
    print(pushDominoes("LL.R"))

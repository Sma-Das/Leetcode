def maxEvents(events: list[list[int, int]]) -> int:
    events = sorted(events, key=lambda x: (x[1] - x[0], x[0], x[1]))
    reserved = set()

    for start, end in events:
        if start not in reserved:
            reserved.add(start)
        else:
            for day in range(start, end+1):
                if day not in reserved:
                    reserved.add(day)
                    break
    return len(reserved)


if __name__ == '__main__':
    events = [
        [[1, 2], [2, 3], [3, 4]],
        [[1, 2], [2, 3], [3, 4], [1, 2]],
        [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]],
        [[1, 100000]],
        [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],
    ]
    for event in events:
        print(maxEvents(event))

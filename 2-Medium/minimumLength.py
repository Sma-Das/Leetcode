from collections import deque


def minimumLength(s):
    string = deque(s)
    while True:
        if string and (duped_letter := string[0]) == string[-1]:
            while string and (left := string.popleft()) == duped_letter:
                pass
            while string and (right := string.pop()) == duped_letter:
                pass
            if right != duped_letter:
                string.append(right)
            if left != duped_letter:
                string.appendleft(left)
        else:
            break
    print("".join(string))
    return len(string)


if __name__ == '__main__':
    print(minimumLength("cabaabac"))

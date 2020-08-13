# 58. length of last word


def lengthOfLastWord(s: str) -> int:
    stack = []
    for i in reversed(s):
        print(stack, i)
        if i != ' ':
            stack.append(i)
        else:
            length = len(stack)
            if length != 0:
                return length
            else:
                continue
    return len(stack)


target = ' '
print(lengthOfLastWord(target))

# split by 8 width, fill 0


def split_8(string):
    result = []
    for i in range(0, len(string), 8):
        sub = string[i:i+8]
        if len(sub) < 8:
            sub = sub + '0' * (8-len(sub))
            result.append(sub)
            break
        else:
            result.append(sub)
    return result


print(split_8('abcde'*5))
print(split_8('abcde'))
print(split_8('abcdefgh'))

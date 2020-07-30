# 7. reverse integer
def reverse(self, x: int) -> int:
    s = str(x)
    flag = s[0] == '-'
    up = 2**31 - 1
    down = -2**31
    r = int(str(abs(x))[::-1])
    if flag:
        r *= -1
    if r > up or r < down:
        return 0
    return r


def reverse2(x):
    def divmod(n, base):
        return n//10, n%10

    up = 2**31 - 1
    down = -2**31
    r = 0
    flag = (x>0)
    if flag == 0:
        flag = -1
    x = abs(x)
    while x > 0:
        x, value = divmod(x, 10)
        r = r * 10 + value
    if down < r < up:
        return r*flag
    else:
        return 0

target = -321
print(reverse2(target))

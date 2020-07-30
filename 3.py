def isPalindrome(x: int) -> bool:
    def divmod(x):
        return x//10, x%10

    if x < 0:
        return False
    r = 0
    while x > r:
        x, value = divmod(x)
        if x == r and x != 0:
            return True
        r = r*10 + value
        print(x, r, value)
    return x == r


target = 1
print(isPalindrome(target))

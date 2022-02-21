def hammingWeight(n: int) -> int:
    n = bin(n)[2:]
    s = str(n)
    count = 0
    for ch in s:
        if ch == "1":
            count = count + 1
    return count

a = 11
print(hammingWeight(a))
def dot_prod(a: str, b: str) -> int:
    s = 0

    for i in range(len(a)):
        s += int(a[i]) * int(b[i])

    return s
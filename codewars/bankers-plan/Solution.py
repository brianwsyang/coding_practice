def fortune(f0, p, c0, n, i):
    # f0: deposit
    # p: interest rate
    # c0: withdrawal
    # n: years
    # i: inflation
    for _ in range(n-1):
        f0 = int(f0 * (1 + p/100) - c0)
        c0 = int(c0 * (1 + i/100))
    
    return f0 >= 0
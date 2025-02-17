def fibo_td(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo_td(n-1, memo) + fibo_td(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    fibo = fibo_td(6)
    print(fibo)    
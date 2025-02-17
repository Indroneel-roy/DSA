def fibo_BU(n):
    dp = [0]*(n+1)
    if n <= 1:
        return n
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]    
if __name__ == "__main__":
    fibo = fibo_BU(5)
    print(fibo)
    
    
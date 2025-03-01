def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)
if __name__ == "__main__":
    fi = fibo(6)
    print(fi)
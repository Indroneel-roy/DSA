def pyramid_pattern(n : int):
    for i in range(1, n+1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
if __name__ == "__main__":
    n = 5
    pyramid_pattern(n)        
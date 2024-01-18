def main():
    N = 10
    print(f"\nФибоначчи({N}) разными функциями:")
    print(f"fib_td({N}) = {fibonacci(N, 'TD')}")
    print(f"fib_bu({N}) = {fibonacci(N, 'BU')}")
    print(f"fib_bu_improved({N}) = {fibonacci(N, 'BU_I')}")

def fibonacci(n, func='TD'):
    f = [0] * (n + 1)

    def fib_td(k):
        if k <= 1:
            f[k] = k
        else:
            f[k] = fib_td(k - 1) + fib_td(k - 2)
        return f[k]

    def fib_bu(k):
        fib = [0] * (k + 1)
        fib[1] = 1
        for i in range(2, k + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[k]

    def fib_bu_improved(k):
        if k <= 1:
            return k
        prev, curr = 0, 1
        for _ in range(1, k):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr

    if func == 'TD':
        f = [0] * (n + 1)
        return fib_td(n)
    elif func == 'BU':
        return fib_bu(n)
    elif func == 'BU_I':
        return fib_bu_improved(n)
    else:
        print(f"Неизвестная функция {func}")
        exit(1)

if __name__ == "__main__":
    main()
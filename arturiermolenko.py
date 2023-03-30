def nthFibo(n):
    K = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        K[i] = K[i - 1] + K[i - 2]
    print(K[n])


nthFibo(6)

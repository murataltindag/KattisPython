t = int(input())

for _ in range(t):
    n = int(input())
    times = [0] * n
    for i in range(n):
        w = list(map(int, input().split()))
        sum = 0
        for j in range(1, len(w)):
            sum += w[j]
        times[i] = sum
    times.sort()
    ans = 0
    for i in range(n):
        ans += times[i] * (n - i)
    print(ans/n)
    
    
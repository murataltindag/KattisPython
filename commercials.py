def max_ending_at_j(j, breaks):
    max_so_far = 0
    sum = 0
    for i in range(j, -1, -1):
        sum += breaks[i]
        if sum > max_so_far:
            max_so_far = sum
        i -= 1
    return max_so_far

while True:
    try:
        n, p = map(int, input().split()) 
    except:
        break
    
    if(n == 0):
        print(0)
        break
    
    breaks = [0] * n
    
    i = 0
    for val in map(int, input().split()):
        breaks[i] = val - p
        i += 1
    
    memo_sum = [0] * (n + 1)
    memo_end = [0] * n
    
    memo_end[n-1] = max_ending_at_j(n-1, breaks)
    
    for i in range(n - 2, -1, -1):
        memo_end[i] = memo_end[i + 1] - breaks[i + 1]
    
    for j in range(1, n + 1):
        memo_sum[j] = max(memo_sum[j - 1], memo_end[j - 1])
    
    print(memo_sum[n])
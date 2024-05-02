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
        
    sum = 0
    max_so_far = 0
    
    for i in range(n):
        sum += breaks[i]
        if sum < 0:
            sum = 0
        if sum < breaks[i]:
            sum = breaks[i]
        if sum > max_so_far:
            max_so_far = sum
            
    print(max_so_far)
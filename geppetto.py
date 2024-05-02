def solve(pizza, i):
    global n, forbidden, valid
    
    if(i == n):
        valid += 1
        return

    solve(pizza, i + 1)
    pizza[i] = 1
    if feasible(pizza):
        solve(pizza, i + 1)
    pizza[i] = 0
    return 
        
def feasible(pizza):
    global n, forbidden
    
    for i in range(n):
        if pizza[i] == 1:
            for j in range(i + 1, n):
                if pizza[j] == 1 and j in forbidden[i]:
                    return False
    return True

while True:
    try:
        n, m = map(int, input().split()) 
    except:
        break
    
    forbidden = {}
    
    for i in range(n):
        forbidden[i] = set()
    
    for i in range(m):
        a, b = map(int, input().split()) 
        a -= 1
        b -= 1
        forbidden[a].add(b)
        forbidden[b].add(a)
    
    pizza = [0] * n  
    valid = 0
    solve(pizza, 0)
    print(valid)
def peek(stack):
    if(len(stack) == 0):
        return -1
        
    tmp = stack.pop()
    stack.append(tmp)
    return tmp

n = int(input())

adj = {}
marked = {}
start_time = {}
end_time = {}

for _ in range(n):
    v1, v2 = input().split()
    if not (v1 in adj.keys()):
        l1 = []
    else:
        l1 = adj[v1]
    l1.append(v2)
    adj[v1] = l1
    marked[v1] = False
    if not (v2 in adj.keys()):
        adj[v2] = []
    marked[v2] = False
    
stack = []
city = input()
clock = 0
dead_end = []

stack.append(city)

while len(stack) > 0:
    dest = stack[-1]  
    if dest in dead_end:
        stack.pop()
        continue
    if not marked[dest]:  
        start_time[dest] = clock
        marked[dest] = 1  
        clock += 1 
    all_visited = True
    for i in adj[dest]:
        if not marked[i]:
            stack.append(i)
            all_visited = False
            break  
    if all_visited:
        dead_end.append(dest)
        clock += 1
        end_time[dest] = clock
        stack.pop()  
    
    
while True:
    if (safe):
        print(city + " safe")
    else:
        print(city + " trapped")
    try:
        city = input()
    except:
        break
    
    
    
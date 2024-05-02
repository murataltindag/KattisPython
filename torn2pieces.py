n = int(input())

adj = {}
marked = {}

for _ in range(n):
    neighbors = input().split()
    v1 = neighbors[0]
    marked[v1] = 0
    for i in range(1, len(neighbors)):
        v2 = neighbors[i]
        marked[v2] = 0
        if(v2 not in adj.keys()):
            adj[v2] = []
        if(v1 not in adj[v2]):
            adj[v2].append(v1)
        if(v1 not in adj.keys()):
            adj[v1] = []
        if(v2 not in adj[v1]):
            adj[v1].append(v2)  
    
stack = []
path = []
whereFrom = {}

start, end = input().split()

marked[start] = 1

for i in adj[start]:
    stack.append(i)
    whereFrom[i] = start

while len(stack) > 0:
    dest = stack.pop()
    if(dest == end):
        curr = end
        while(curr in whereFrom.keys()):
            path.append(curr)
            curr = whereFrom[curr]
        break
    elif not marked[dest]:
        marked[dest] = 1
        for i in adj[dest]:
            if not marked[i]:
                stack.append(i)
                if(i not in whereFrom.keys()):
                    whereFrom[i] = dest
    
path.append(start)

if(len(path) < 2):
    print("no route found")  
else:
    for i in range(len(path)-1, -1,-1):
        print(path[i], end=" ")
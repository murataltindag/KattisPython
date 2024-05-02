def dfs(v, clock):
    global G, mark, pre, post
    mark.add(v)
    clock += 1
    pre[v] = clock
    for u in G[v]:
        if u not in mark:
            clock = dfs(u, clock)
    clock += 1
    post[v] = clock
    return clock

n = int(input())
G, pre, post = {}, {}, {}
for i in range(n):
    u, *vlist = input().split()
    u = u[:-1]
    for v in vlist:
        if u not in G:
            G[u] = []
        if v not in G:
            G[v] = []
        G[v].append(u)
    pre[u] = post[u] = 0
    
mark = set()
start = input()
clock = 0
clock = dfs(start, clock)

sorted_post = dict(sorted(post.items(), key=lambda item: item[1], reverse=True))

for v in sorted_post:
    if post[v] != 0:
        print(v)
import heapq
from collections import deque

l = list(map(int, input().split()))
n = l[0]
v = l[-1]

capacities = sorted(l[1:-1], reverse=True)
start_list = [0] * n
start_list[0] = capacities[0]

start = tuple(start_list)

Graph = {} 
Graph[start] = []
Weight = {}
Weight[start] = []
    
queue = deque([start])
visited = set([start])

while queue:
    current = queue.popleft()
    for i in range(n):
        for j in range(n):
            if i != j:
                new_state = list(current)
                pour = min(new_state[i], capacities[j] - new_state[j])
                new_state[i] -= pour
                new_state[j] += pour
                new_state = tuple(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
                    Graph.setdefault(current, []).append(new_state)
                    Weight.setdefault(current, []).append(pour)
                    Graph.setdefault(new_state, []).append(current)
                    Weight.setdefault(new_state, []).append(pour)    

dist = {start: 0}
heap = [(0, start)]

while heap:
    current_dist, current = heapq.heappop(heap)
    if current_dist != dist[current]:
        continue
    for i in range(n):
        for j in range(n):
            if i != j:
                new_state = list(current)
                pour = min(new_state[i], capacities[j] - new_state[j])
                new_state[i] -= pour
                new_state[j] += pour
                new_state = tuple(new_state)
                new_dist = current_dist + pour
                if new_state not in dist or new_dist < dist[new_state]:
                    dist[new_state] = new_dist
                    heapq.heappush(heap, (new_dist, new_state))

min_dist = float('inf')
goal_state = None
for state, distance in dist.items():
    if state[0] == v and distance < min_dist:
        min_dist = distance
        goal_state = state

if min_dist == float('inf'):
    print("impossible")
else:
    print(min_dist)
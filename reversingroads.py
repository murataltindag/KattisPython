def scc(graph):
    n = len(graph)
    reversed_graph = {i: [] for i in range(n)}
    for u in range(n):
        for v in graph[u]:
            reversed_graph[v].append(u)

    visited = [False] * n
    postorder = []

    for v in range(n):
        if not visited[v]:
            dfs(v, reversed_graph, visited, postorder)

    postorder.reverse()

    visited = [False] * n
    sccs = []
    for v in postorder:
        if not visited[v]:
            scc = []
            dfs(v, graph, visited, scc)
            sccs.append(scc)

    vertex_to_scc = [0] * n
    for i, scc in enumerate(sccs):
        for vertex in scc:
            vertex_to_scc[vertex] = i

    scc_graph = {i: [] for i in range(len(sccs))}
    in_degrees = [0] * len(sccs)
    out_degrees = [0] * len(sccs)

    for u in range(n):
        for v in graph[u]:
            if vertex_to_scc[u] != vertex_to_scc[v]:
                scc_graph[vertex_to_scc[u]].append(vertex_to_scc[v])
                out_degrees[vertex_to_scc[u]] += 1
                in_degrees[vertex_to_scc[v]] += 1

    sources = sum(1 for deg in in_degrees if deg == 0)
    sinks = sum(1 for deg in out_degrees if deg == 0)

    return sources, sinks, sccs, vertex_to_scc, in_degrees, out_degrees

def dfs(v, reversed_graph, visited, postorder):
    visited[v] = True
    for u in reversed_graph[v]:
        if not visited[u]:
            dfs(u, reversed_graph, visited, postorder)
    postorder.append(v)

count = 1

while True:
    try: n, m = map(int, input().split())
    except: break
    
    graph = {i: [] for i in range(n)}

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    sources, sinks, sccs, vertex_to_scc, in_degrees, out_degrees = scc(graph)

    if len(sccs) == 1:
        print(f"Case {count}: valid")
    elif sources == 1 and sinks == 1:
        source_component = [i for i, deg in enumerate(in_degrees) if deg == 0][0]
        sink_component = [i for i, deg in enumerate(out_degrees) if deg == 0][0]

        for u in range(n):
            if vertex_to_scc[u] == source_component:
                for v in graph[u]:
                    if vertex_to_scc[v] == sink_component:
                        print(f"Case {count}: {u} {v}")
                        break
                else:
                    continue
                break
        else:
            print(f"Case {count}: invalid")
    else:
        print(f"Case {count}: invalid")
    count += 1
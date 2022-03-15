from typing import List, Dict
import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def debug(*args):
    print(*args, file=sys.stderr)

def solution(graph: Dict[int, List[int]]) -> List[int]:
    n = len(graph)
    low=[-1]*n
    disc=[-1]*n
    visited=set()
    res=[]
    p = [None]*n
    def dfs(node,parent,timer):
        nonlocal low,graph,res,visited,disc
        count = 0
        p[node] = parent
        low[node]=timer
        disc[node]=timer
        visited.add(node)
        timer += 1
        for child in graph[node]:
            if disc[child] == -1:
                count +=1
                p[child] = node
                dfs(child, node, timer)
                low[node] = min(low[node], low[child])
                if p[node] == -1 and count >1:
                    res.append(node)
                if p[node] != -1 and low[child] >= disc[node]:
                    res.append(node)
            elif child != p[node]:
                low[node] = min(low[node], disc[child])
            
    dfs(0,-1,0)
    return res


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        debug(f"Test #{t}:")
        N, M = map(int, input().split())
        graph = {i: [] for i in range(N)}
        for _ in range(M):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        pts = solution(graph)
        print(" ".join(map(str, sorted(set(pts)))))

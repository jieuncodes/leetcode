# First approach - wrong when very long input (not time limit exceeded)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        rev_edges = [[b,a] for a,b in edges]
        edges = edges + rev_edges
        succProb = 2* succProb

        self.max_prob = 0
    
        def dfs(target, path_prob, visited):

            visited.add(target)
            for edge, prob in zip(edges, succProb):
                if edge[0] == target and edge[1] not in visited:
                    if edge[1] == end :
                        self.max_prob = max(self.max_prob, path_prob * prob)
                    else:
                        dfs(edge[1], path_prob * prob, visited)
            
        dfs(start, 1, set())

        return self.max_prob



# BFS is not suitable for finding the maximum or minimum path in a graph with weights. BFS is perfect for finding the shortest path in a graph without weights. 
# For finding the shortest path in a graph with weights, we typically use Dijkstra's algorithm or the Bellman-Ford algorithm (greedy method).

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst,succProb[i]])
            adj[dst].append([src,succProb[i]])

        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return prob * -1
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq,(prob * edgeProb, nei))

        return 0
    

# Bellman-Ford algorithm
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        max_prob = [0] * n
        max_prob[start] = 1
        
        for i in range(n - 1):
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1 
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1

            if not has_update:
                break
        
        return max_prob[end]
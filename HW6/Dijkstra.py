from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        self.graph.append([u,v,w])
        
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
        dist = dict()
        for i in range(self.V):
            dist[str(i)] = float("Inf")
        dist[str(s)] = 0
        
        Queue = [False] * self.V
        
        for cnt in range(self.V):
            u = self.ExtractMin(dist, Queue)
            Queue[u] = True
            for v in range(self.V): #relax
                if self.graph[u][v]>0: #adj[u] edge
                    if Queue[v] == False:
                        if dist[str(v)] > dist[str(u)] + self.graph[u][v]:
                            dist[str(v)] = dist[str(u)] + self.graph[u][v]
        return dist                    
        
    def ExtractMin(self, dist, Queue):
        Min = float("Inf")
        for v in range(self.V):
            if dist[str(v)] < Min and Queue[v] == False:
                Min = dist[str(v)]
                min_index = v
        return min_index
        
    def Kruskal(self):
        """
        :rtype: dict
        """
        result = dict()
        e = 0
        self.graph.sort(key=lambda item:item[2])
        #x = sorted(self.graph, key=lamba item:item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        for u,v,w in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x!=y:
                e = e + 1
                result['%d%s%d' %(u,'-',v)] = w
                if e==self.V -1:
                    break
                self.union(parent, rank, x, y)
        return result
        
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
        
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        else:
            parent[yroot] = xroot
            if rank[xroot] == rank[yroot]:
                rank[xroot] += 1
        

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];

print("Dijkstra:", g.Dijkstra(0))
        
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print("Kruskal", g.Kruskal())
#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict 
  

class Graph:

    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  

    def BFS(self, s): 
        if s in self.graph:
            queue = [s]
            visited = []

            while queue:
                current = queue.pop(0)
                visited.append(current)
                for i in self.graph[current]:
                    if i not in queue and i not in visited:
                        queue.append(i)

            return visited
        else:
            print("Wrong start!")
            
        
    def DFS(self, s):
        if s in self.graph:
            stack = [s]
            visited = []
            while stack:
                current = stack.pop()
                visited.append(current)
                for i in self.graph[current]:
                    if i not in stack and i not in visited:
                        stack.append(i)
            return visited
        else:
            print("Wrong start")


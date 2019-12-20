#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

            
            
# 參考網站：https://video.search.yahoo.com/yhs/search;_ylt=AwrWnLnUMPxdEkAAywEPxQt.;_ylu=X3oDMTEycmM5NzVzBGNvbG8DZ3ExBHBvcwMzBHZ0aWQDQjg0OTJfMQRzZWMDc2M-?p=BFS&fr=yhs-domaindev-st_emea&hspart=domaindev&hsimp=yhs-st_emea#id=2&vid=5b88b4ccb7aa180c4e3a3365373ea8c0&action=view


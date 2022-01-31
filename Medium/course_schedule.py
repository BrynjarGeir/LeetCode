class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = Graph(numCourses)
        for pre in prerequisites:
            g.addEdge(pre[0],pre[1])
        
        return not g.isCyclic()
                
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False
    
    def isCyclic(self):
        visited = [False] * self.v
        recStack = [False] * self.v
        for node in range(self.v):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
    
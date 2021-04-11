class Graph:


    graph_dict = []

    def addEdge(self,neighborList):
        self.graph_dict.append(neighborList)

class TopoSort:

    def __init__(self,graph):
        self.graph = graph
        self.topo =[]
        self.visited = [False]*len(self.graph)

    def dfs(self,node):
        if self.visited[node]:
            return
        else:
            self.visited[node] = True
            for adjNode in self.graph[node]:
                self.dfs(adjNode)
            self.topo.append(node)

    def getTopoSort(self):
        for i in range(0,len(self.graph)):
            self.dfs(i)
        while len(self.topo)!=0:
            print(self.topo.pop())



if __name__ == '__main__':
    g = Graph()

    edges = [[2,3],[],[],[1],[2,1],[0,2]]
    for edge in edges:
        g.addEdge(edge)
    print(g.graph_dict)
    topo = TopoSort(g.graph_dict)
    topo.getTopoSort()
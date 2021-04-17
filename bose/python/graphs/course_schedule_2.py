class Graph:

    def __init__(self):
        self.graph_dict = {}

    def createGraph(self,numCourses,edgeList):

        for i in range(0,numCourses):
            for j in edgeList:
                if j[1]==i:
                    if i in self.graph_dict:
                        self.graph_dict[i].append(j[0])
                    else:
                        self.graph_dict[i] = [j[0]]
            if i not in self.graph_dict:
                self.graph_dict[i] = []
        # for i in range(0,len(edgeList)):
        #     self.addEdge(edgeList[i][1],edgeList[i][0])

        # for i in range(0,len(edgeList)):
        #     if edgeList[i][0] not in self.graph_dict:
        #         self.graph_dict[edgeList[i][0]] = []
        return self.graph_dict
        
    def addEdge(self,node,adj):
        if node not in self.graph_dict:
            self.graph_dict[node] = [adj]
        else:
            self.graph_dict[node].append(adj)

class TopoSort:
    def __init__(self,numCourses,prerequisites):
        self.g = Graph()
        self.prerequisites = prerequisites
        self.graph = self.g.createGraph(numCourses,self.prerequisites)
        print("Graph is :: {}".format(self.graph))
        self.topo =[]
        self.visited = [False]*numCourses

    def dfs(self,node):
        if self.visited[node]:
            return
        else:
            self.visited[node] = True
            if node in self.graph:
                for adjNode in self.graph[node]:
                    self.dfs(adjNode)
            self.topo.append(node)

    
    def getTopoSort(self):
        for i in self.graph:
            self.dfs(i)
        self.topo.reverse()
        return self.topo
            
            


if __name__ == '__main__':
    # g = Graph()
    # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    # numCourses = 4

    prerequisites = [[1,0]]
    numCourses = 3
    # prerequisites = []
    # numCourses = 1
    # for i in range(0,len(prerequisites)):
    #     g.addEdge(prerequisites[i][1],prerequisites[i][0])

    # print("The graph is :: {}".format(g.graph_dict))
    topo = TopoSort(numCourses,prerequisites)
    print(topo.getTopoSort())

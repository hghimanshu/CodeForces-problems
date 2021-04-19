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
        return self.graph_dict
        
    def addEdge(self,node,adj):
        if node not in self.graph_dict:
            self.graph_dict[node] = [adj]
        else:
            self.graph_dict[node].append(adj)

class DetectCycle:

    def __init__(self,graph):
        self.graph = graph

    def isCyclicUtil(self,node,visited):
        visited[node] =1

        for adjNode in self.graph[node]:
            if visited[adjNode] ==1:
                return True
            if visited[adjNode]==0:
                check = self.isCyclicUtil(adjNode,visited)
                if check:
                    return True
        visited[node] = 2
        return False


    def isCyclic(self):
        visited = [0]*len(list(self.graph))

        for node,val in self.graph.items():
            if visited[node]==0:
                check = self.isCyclicUtil(node,visited)
                if check:
                    return True
        return False

if __name__ == "__main__":
    g = Graph()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    g.createGraph(numCourses,prerequisites)
    print(g.graph_dict)
    det = DetectCycle(g.graph_dict)
    print(det.isCyclic())
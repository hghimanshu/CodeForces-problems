class Graph:

    graph_dict = {}

    def addEdge(self,node,neighbor):
        if node not in self.graph_dict:
            if neighbor !="":
                self.graph_dict[node] = [neighbor]
            else:
                self.graph_dict[node] = []
        else:
            self.graph_dict[node].append(neighbor)


class DetectCycle:

    def __init__(self,graph):
        self.graph = graph

    def isCyclicUtil(self,node,visited):
        visited[node] = 1

        for adjNode in self.graph[node]:
            if visited[adjNode]==1:
                return True
            if visited[adjNode]==0:
                check = self.isCyclicUtil(adjNode,visited)
                if check:
                    return True
        visited[node] = 2
        return False

    def isCyclic(self):
        visited = [0]*len(list(self.graph.keys()))

        for node,idx in self.graph.items():
            if visited[node]==0:
                check = self.isCyclicUtil(node,visited)
                if check:
                    return True
        return False


if __name__ == '__main__':
    g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 3)
    # g.addEdge(0, 2)
    # g.addEdge(2, 3)
    # g.addEdge(2, 0)
    # g.addEdge(1, 0)
    # g.addEdge(3, 0)
    # g.addEdge(3, 2)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, "")
    g.addEdge(1, 3)
    # g.addEdge(3, 2)
    # g.addEdge(3, 1)
    g.addEdge(3, "")
    print(g.graph_dict)
    det = DetectCycle(g.graph_dict)
    print(det.isCyclic())
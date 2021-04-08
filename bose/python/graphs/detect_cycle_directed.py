class Graph:

    graph_dict ={}


    def addEdge(self,node,neighbor):
        if node not in self.graph_dict:
            if neighbor !="":
                self.graph_dict[node] = [neighbor]
            else:
                self.graph_dict[node] = []
        else:
            self.graph_dict[node].append(neighbor)



class DetectCycle:

    def isCyclicUtil(self,graph,curr,visited):
        if visited[curr]:
            return True
        for adjNode in graph[curr]:
            check = self.isCyclicUtil(graph,adjNode,visited)
            if check:
                return True
        return False

    def isCyclic(self,graph):
        visited = {}
        for key,val in graph.items():
            visited[key] = False
        
        for node in graph:
            visited[node] = True
            # for i in range(0,len(graph[node])):
            for adjNode in graph[node]:
                print("Curr node is :: {} and adjNode is :: {}".format(node, adjNode))
                check = self.isCyclicUtil(graph,adjNode,visited)
                if check:
                    return True
            visited[node] = False
        return False


if __name__ == '__main__':
    g = Graph()
    g.addEdge('0', '1')
    g.addEdge('1', "")
    g.addEdge('2', '1')
    g.addEdge('2', '3')
    g.addEdge('3', '4')
    # g.addEdge('4', '2')
    g.addEdge('4', '0')
    det = DetectCycle()
    print("Cycle is present:: {}".format(det.isCyclic(g.graph_dict)))
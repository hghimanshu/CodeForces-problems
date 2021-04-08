class Node:
    def __init__(self,val=0,neighbors=None):
        self.val=val
        self.neighbors=neighbors
 
class Graph:

    graph_dict = {}

    def addNode(self,val,neighbors=None):

        for node in self.graph_dict:
            if node.val == val:
                print("Node found with val :: {}".format(node.val))
                print("Current node neighbors are :: {}".format(node.neighbors))
                print("Current neighbors in graph are :: {}".format(self.graph_dict[node]))
                node.neighbors+=neighbors
            
                self.graph_dict[node]=node.neighbors
                return 1
        
        newNode = Node(val)
        if not neighbors:
            neighbors = []
        newNode.neighbors = neighbors 
        self.graph_dict[newNode]=newNode.neighbors
        
def clone_graph(self,node):

    if not node:
        return None
        
    q = []
    vertex_map= {}
    vertex_map[node]=Node(node.val)
    
    q = [node]
    
    while q:
        s=q.pop(0)
        for e in s.neighbors:
            if e not in vertex_map:
                vertex_map[e] = Node(e.val)
                q.append(e)
            vertex_map[s].neighbors.append(vertex_map[e])
            print("Vertex map is :: {}".format(vertex_map))
    return vertex_map[node]




    # def addEdge(self,val,neighbor=None):
    #     node = Node(val)
    #     if node not in self.graph_dict:
    #         self.graph_dict.update({node:})
    #         self.graph_dict[node].neighbors = [neighbor]
    #     else:
    #         self.graph_dict[node].neighbors.append(neighbor)


    # def show_edges(self):
    #     for node in self.graph_dict:
    #         for neighbor in self.graph_dict[node].neighbors:
    #             print("( "+node.val+","+neighbor+")")
            


if __name__ == "__main__":
    g= Graph()
    g.addNode(1,[2,4])
    g.addNode(2,[1,3])
    g.addNode(3,[2,4])
    g.addNode(4,[1,3])
    print(g.graph_dict)
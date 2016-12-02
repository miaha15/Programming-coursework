'''https://en.wikipedia.org/wiki/Dijkstra's_algorithm'''
'https://www.python.org/doc/essays/graphs/'
'http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python'
'http://www.bogotobogo.com/python/python_graph_data_structures.php'
'http://www.python-course.eu/graphs_python.php'
'Diana Lecture Slides'


class Node:
    def __init__(self, value):
        self.vertex = value

class Adding:
    def addVertex(self, v):
        
        for array in self.edge:
            array.append(0)
        self.edge.append([0] * (len(self.edge) + 1))
        self.edgeID[v.vertex] = len(self.edgeID)


    def addEdge(self, vertice, edge, weight):
        self.edge[self.edgeID[vertice]][self.edgeID[edge]] = weight
        self.edge[self.edgeID[edge]][self.edgeID[vertice]] = weight


class Graph(Adding, object):
    def __init__(self):
        self.edge = []  
        self.edgeID = {}

    def ShowGraph(self):
        print("Displayed Graph")
        
        for KeyValue in self.edgeID:
            print("Node: ", KeyValue)

    def Dijkstra(self, start, destination):
        StartPos = start
        travelled = {}  
        Last = {}  
        travelled2 = {}  
        base = sorted(self.edgeID.keys())
        
        for element1, element2 in self.edgeID.items():
            travelled[element1] = 500  
            travelled2[element1] = 500
            Last[element1] = "Not Visited"  
        travelled[start] = 0     
        travelled2[start] = 0
        
        while len(base) != 0:
            current_shortest_path = min(travelled2.values())
            
            for node, distance in travelled2.items():
                if distance == current_shortest_path:   
                    content = node
                    base.remove(node)      
                    del(travelled2[node])
                    break
                
            possibilities = self.edge[self.edgeID[content]]  
            position = -1
            
            for connected in possibilities:  
                position = position + 1
                if connected != 0:  
                    DiffRoute = travelled[content] + connected
                    
                    if DiffRoute < travelled[sorted(self.edgeID)[position]]:  
                        Neighbour = sorted(self.edgeID)
                        Last[Neighbour[position]] = content  
                        start = Neighbour[position]  
                        travelled2[start] = DiffRoute  
                        travelled[start] = DiffRoute
                        
        pathfinder(Last, StartPos, destination)
        print("Total distance =", travelled[destination])


def pathfinder(LastNode, StartNode, Location):
    path = [Location]  
    while path[len(path) - 1] != StartNode:  
        for element3, element4 in LastNode.items():  
            if element3 == Location and element4 != StartNode:
                
                if element3 not in path:   
                    path.append(element4)  
                Location = element4
                
            elif element3 == Location and element4 == StartNode: 
                path.append(element3)  
                path.append(StartNode)
                
    path.reverse()  
    print("Shortest Path Traversed: ", path)
    file = open("Shortest_Path.txt", "w")
    file.write(str(path))
    file.close()
    return path


if __name__ == '__main__':
    G = Graph()
    G.addVertex(Node('A'))
    G.addVertex(Node('B'))
    G.addVertex(Node('C'))
    G.addVertex(Node('D'))
    G.addVertex(Node('E'))
    
    NodeValues = ['F', 'G', 'H', 'I', 'J']
    
    for each in NodeValues:
        G.addVertex(Node(each))
        
    G.addEdge('A', 'B', 3) 
    G.addEdge('A', 'C', 2)
    G.addEdge('A', 'F', 4)
    G.addEdge('A', 'G', 5)
    G.addEdge('B', 'C', 6)
    G.addEdge('B', 'D', 8)
    G.addEdge('C', 'D', 9)
    G.addEdge('C', 'F', 2)
    G.addEdge('D', 'E', 5)
    G.addEdge('D', 'I', 9)
    G.addEdge('E', 'F', 1)
    G.addEdge('F', 'G', 5)
    G.addEdge('F', 'H', 6)
    G.addEdge('H', 'E', 2)
    G.addEdge('J', 'I', 7)
    G.addEdge('J', 'A', 1)
    G.ShowGraph()
    
    G.Dijkstra(input("Enter Start Node(CAPITAL LETTERS ONLY: "),(input("Enter Destination Node(CAPITAL LETTERS ONLY: ")))


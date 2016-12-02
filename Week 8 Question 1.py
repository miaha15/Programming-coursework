'''https://en.wikipedia.org/wiki/Dijkstra's_algorithm'''
'https://www.python.org/doc/essays/graphs/'
'http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python'
'http://www.bogotobogo.com/python/python_graph_data_structures.php'
'http://www.python-course.eu/graphs_python.php'
'Diana Lecture Slides'

'''
EDGES are stored in a list between nodes in self.edge
LOCATION of the edges are stored in a list called self.edgeID

self.edge[self.edgeID[vertice]][self.edgeID[edge]] updates the list
self.edge[self.edgeID[edge]][self.edgeID[vertice]] points to the specific
value in the list to be updated

DIJKSTRA

distance of nodes from the start node stored in the dictionary travelled{}
shortest path of nodes which connect to each other is stored in Last{}
the next distance of the next node from the start node is stored in a different
dictionary called travelled2{}

DISTANCE dictionary is set all distances to 500 of how many they can travel up to
could put 999 which is the max but there is no need as it may never go that far

if distance == shortestpathfound: checks to see if the current path is the shortest path
to the destination node

base.remove(node) removes both the base and the distance travelled as there are no other shorter
paths discoverable.

break used to make sure that the while loop is exited completely and does not continuously loop

possibilities = self.edge[self.edgeID[content]] this is where all the connections found to the
destination node are stored

position = -1 is used to hold the position inside possibilities

for connected in possibilities:  this for loop checks each possible connection discoverable to the
destination node

StartPos is the start node, destination is the end node you want to reach in the shortest path

Diffroute is used to store the other different paths available to the destination node

next line checks to see if the new path found is shorter than the last recent path find

path = [location] is created to find the path

while loop then loops until the start nide is reached, reads back from the destination to the
start node
'''

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
        
        for element1, element2 in self.edgeID.items(): #items returns the dictionary
            travelled[element1] = 500  
            travelled2[element1] = 500
            Last[element1] = "Not Visited"  
        travelled[start] = 0     
        travelled2[start] = 0
        
        while len(base) != 0:
            shortestpathfound = min(travelled2.values())
            
            for node, distance in travelled2.items():
                if distance == shortestpathfound:   
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
            if element3 == Location and element4 != StartNode: #when location of the start node is found
                
                if element3 not in path:   
                    path.append(element4)  #adds the route to the start node into path
                Location = element4
                
            elif element3 == Location and element4 == StartNode: #node to be reached next is the start node
                path.append(element3)  
                path.append(StartNode) #adds the start node and location to the end of path variable
                
    path.reverse()  #reads the variable backwards
    print("Shortest Path Traversed: ", path)
    file = open("Shortest_Path.txt", "w")
    file.write(str(path))
    file.close() #saves traversed shortest path to a text file
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
    G.ShowGraph() #displays the nodes stored for the user to then choose the start and destination node
    
    G.Dijkstra(input("Enter Start Node(CAPITAL LETTERS ONLY: "),(input("Enter Destination Node(CAPITAL LETTERS ONLY: ")))


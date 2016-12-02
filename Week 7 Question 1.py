'https://www.youtube.com/watch?v=HDUzBEG1GlA'
'http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/'

'''PSEUDO CODE

procedure VERTEX

    __INIT__
        dictionary <- {}

    ADDVERTEX [V]
        IF V not in dictionary THEN
            dictionary[V] <- []

    ADDEDGE [V,E]
        dictionary[V] add to the end [E]
        dictionary[E] add to the end [V]

procedure GRAPH [VERTEX]

    SHOWGRAPH
        OUTPUT message

        FOR i in dictionary DO
            OUTPUT[i, dictionary[i]]

if ___name___ EQUALS '__main__' THEN

        G <- GRAPH()

        G.ADDVERTEX['A']
        G.ADDVERTEX['B']
        .
        .
        .
        .
        .
        .
        .
        G.ADDEDGE['A', 'B']
        .
        .
        .
        .
        .
        .
        .

        OUTPUT message

        G.SHOWGRAPH()
'''

'''
dictionary is set to an empty tuple when first called during the instantiation
When adding a vertex, if its not in the dictionary it will get added
When adding an edge, it will add the edge to the vertex dictionary and add the
vertex to the edge dictionary to create a link/relationship.

for each value in the dictionary it will print all associated nodes to that vertex

BFS uses a QUEUE of vertices that have been found and also the ones that havent
been visited yet and then constantly visits the front of the vertex of the queue
finding its connecting neighbours and adding them to the end of the queue

AKA vertex found sooner are visited sooner.

DFS uses a STACK, new vertices are visited straight away and vertices that were
found previously are only returned back to when the new vertices have been visited.
This makes it so that it it searches the path one vertice before checking other
vertice' paths.

when saving the traversed nodes, a new file is created with the given name where it
stores the visited vertices by writing them in the text file.
This text file is written over if it is called again by the new traversed nodes.

'''

import sys

class Vertex:

    def __init__(self):
        self.dictionary = {}
        
    def addVertex(self,vertex):
        if vertex not in self.dictionary:
            self.dictionary[vertex] = []
        
    def addEdge(self,vertex,edge):
        self.dictionary[vertex].append(edge)
        self.dictionary[edge].append(vertex)


class Graph(Vertex):

    def ShowGraph(self):
        print("Displayed Graph")
        
        for KeyValue in self.dictionary:
            print(KeyValue, ':', self.dictionary[KeyValue])

    def BreadthFirstSearch(self,vertex):

        self.queue = []
        self.visited = []

        self.queue.insert(0, vertex)

        while self.queue != []:
            Queue = self.queue.pop()
            if Queue not in self.visited:
                self.visited.append(Queue)
                for edge in self.dictionary[Queue]:
                    self.queue.insert(0,edge)
        print (self.visited)
        file = open("BreadthFirst.txt", "w")
        file.write(str(self.visited))
        file.close()
        return self.visited
       

    def DepthFirstSearch(self, vertex):
        
        self.visited = []
        self.stack = []

        self.stack.append(vertex)

        while self.stack != []:
            Stack = self.stack.pop()
            if Stack not in self.visited:
                self.visited.append(Stack)
                for edge in self.dictionary[Stack]:
                    self.stack.append(edge)
                file = open("DepthFirst.txt", "w")
                file.write(str(self.visited))
                file.close()
        print(self.visited)
        return(self.visited)
        

if __name__ == '__main__':
    
    G = Graph()

    G.addVertex('A')
    G.addVertex('B')
    G.addVertex('C')
    G.addVertex('D')
    G.addVertex('E')
    G.addVertex('F')
    G.addVertex('G')
    G.addVertex('H')
    G.addVertex('I')
    G.addVertex('J')

    G.addEdge('A', 'B')  
    G.addEdge('A', 'C')
    G.addEdge('A', 'F')
    G.addEdge('A', 'G')
    G.addEdge('B', 'C')
    G.addEdge('B', 'D')
    G.addEdge('C', 'D')
    G.addEdge('C', 'F')
    G.addEdge('D', 'E')
    G.addEdge('D', 'I')
    G.addEdge('E', 'F')
    G.addEdge('F', 'G')
    G.addEdge('F', 'H')
    G.addEdge('H', 'E')
    G.addEdge('J', 'I')
    G.addEdge('J', 'A')
    G.ShowGraph()
    
    print("Depth First Search for C")
    G.DepthFirstSearch('C')

    print("Breadth First Search for C")
    G.BreadthFirstSearch('C')

sys.exit()

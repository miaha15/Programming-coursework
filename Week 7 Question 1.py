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

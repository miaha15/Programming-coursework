class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):


    def get_vertex(self, n):


    def add_edge(self, frm, to):


if __name__ == "__main__":

    g = {"a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"]}
    v = Vertex(4)
    r = Vertex(6)
    print(r.id)

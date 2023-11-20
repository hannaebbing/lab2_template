#adjlist={A:[B,D,E],B:[A,C,E],C:[B,D,F],D:[A,C,E,F],E:[A,B,D,F],F:[C,D,E]}
class Graph:
    def __init__(self, start=None, values = None, directed=False):
        self._adjlist = {A:[B,D,E],B:[A,C,E],C:[B,D,F],D:[A,C,E,F],E:[A,B,D,F],F:[C,D,E]}
        if values is None:
            values = {}
        self._valuelist = values
        self._isdirected = directed
        # plus some code for building a graph from a ’start’ object
        # such as a list of edges
        # here are some of the public methods to implement

    def vertices(self):
        return self._adjlist.keys()

    def edges(self):
        pass


    def __len__():
        pass

    def neighbours(self,v):
        pass

    def add_edge(self,a,b):
        pass

    def add_vertex(self,a):
        pass

    def is_directed(self):
        pass

    def get_vertex_value(self, v):
        pass

    def set_vertex_value(self, v, x):
        pass

class WeightedGraph(Graph):

    def set_weight(self, a, b, w):
        pass
    def get_weight(self, a, b):
        pass
    	# etc etc
    	# check the lab assignment for details


if __name__ == "__main__":
    print(Graph.vertices())
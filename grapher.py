from graph import Graph, Vertex, Edge

class Grapher:
    def __init__(self, edges=None, nodes=None, graph=None):
        """Init method for Router."""
        self.edges = edges
        self.nodes = nodes
        self.graph = graph

    def populate_edges(self, edges_list):
        """Populate a list with Edge objects, mapped from db."""
        edges = []
        for edge in edges_list:
            source, target, weight = edge[4], edge[5], edge[6]
            freq, line, geom = edge[7], edge[1], edge[2]
            edges.append(Edge(source, target, weight,
                              freq, line, geom))
        self.edges = edges

    def populate_vertices(self, vertices_list):
        """Populate a list with Vertex objects, mapped from db."""
        vertices = []
        for vertex in vertices_list:
            vertex_id = vertex[0]
            vertices.append(Vertex(vertex_id))
        self.vertices = vertices        

    def populate_graph(self):
        """Populate the graph, using a list of Edges."""
        if self.edges and self.vertices:
            graph = Graph()
            for edge in self.edges:
                graph.add_edge(edge)
            self.graph = graph
        else:
            print("Populate edges & vertices first, then populate graph!")

from exporter import Exporter
from grapher import Grapher
from dijkstra import Dijkstra

class Isochroner():
    def __init__(self, grapher, starting_vertex):
        self.grapher = grapher
        self.dijkstra = Dijkstra(grapher.graph)
        self.starting_vertex = starting_vertex  
        self.geoms_to_lines = self.assign_geoms_to_lines()
 
    def assign_geoms_to_lines(self):
        geom_aggregator = []
        for edge in self.grapher.edges:
            geom_aggregator.append([edge.line(), edge.source(), edge.target()])
        bus_lines = [row[0] for row in geom_aggregator]
        bus_lines = set(bus_lines)
        geom_to_lines = {line:[] for line in bus_lines}
        for row in geom_aggregator:
            geom_to_lines[row[0]].append((row[1],row[2]))
        return geom_to_lines
    
    def is_line_in_edge(self, line, edge):
        return edge in self.geoms_to_lines[line]
 
    def create_isochrones(self):
        isochrones = []
        start = self.starting_vertex
        for vertex in self.grapher.graph.vertices():
            if vertex != start: 
                isochrones.append(self.dijkstra.min_path(start, vertex))
        return isochrones

if __name__=="__main__":
    # Export edges and vertices from qgis database
    def is_same_line(line1, line2):
        return line1 == line2  

    def is_line_in_edge(line, source, target):
        return (source, target) in geoms_to_lines[line]

    def correct_route(route, boarded_line, remaining_route, counter):
	if len(remaining_route) == 1:
            return route
        counter = counter + 1
	cur_edge = remaining_route[0] 
	cur_line = cur_edge.line()
	remaining_route = remaining_route[1:]	
	# print route
	if is_same_line(boarded_line, cur_line):
            # print("Same Line")
            correct_route(route, boarded_line, remaining_route, counter)

	elif is_line_in_edge(boarded_line, cur_edge.source(), cur_edge.target()):
            route[counter]._line = cur_line
            # print("Line Corrected")
            correct_route(route, boarded_line, remaining_route, counter)
	else:
            # print("Changed Bus")
            boarded_line = cur_edge.line()
            correct_route(route, boarded_line, remaining_route, counter)

    e = Exporter()
    db_edges = e.get_edges()
    db_vertices = e.get_vertices()
    # Initialize graph and populate it
    g = Grapher()
    g.populate_vertices(db_vertices)   
    g.populate_edges(db_edges)
    g.populate_graph()
    d = Dijkstra(g.graph)
    i = Isochroner(g, 3)
    route = d.min_path(444, 728)
    route = route[1]
    geoms_to_lines = i.geoms_to_lines
    init_route = route
    init_line = route[0].line()
    init_size = len(route)
    cur_line = init_line 
    counter = 0
    corrected_route = correct_route(route, 'A7', route, 0)
         
     

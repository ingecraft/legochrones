import psycopg2

class Connector:
    def __init__(self, host='localhost', dbname='split_a', user='user', pwd='user'):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.pwd = pwd
    
    def conn_string(self):
        conn_string = "host={} dbname={} user={} password={}".format(self.host,
                      self.dbname, self.user, self.pwd)
        return conn_string

    def get_cursor(self):
        conn = psycopg2.connect(self.conn_string())
        cursor = conn.cursor()
        return cursor

class Exporter:
    """Export edges and vertices from qgis db."""
    queries = {'edges': "SELECT * FROM oasa_a_spl;",
               'vertices':"SELECT * FROM oasa_a_spl_vertices_pgr;",
              }
    
    def get_list_from(self, query):    
        """Return a list from the results of a select query."""
        connector = Connector()
        cursor = connector.get_cursor()
        query_list = []
        cursor.execute(query)
        for row in cursor:
            query_list.append(row)
        cursor.close()
        return [list(item) for item in query_list]

    def get_edges(self):
        """Return edges list."""
        return self.get_list_from(Exporter.queries['edges'])

    def get_vertices(self):
        """Retrun vertices list."""
        return self.get_list_from(Exporter.queries['vertices'])


 

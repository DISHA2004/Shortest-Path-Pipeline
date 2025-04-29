import csv
import networkx as nx

def load_graph_csv(file_path):
    g=nx.Graph()

    with open(file_path, mode='r') as file:
        reader= csv.DictReader(file)
        for row in reader:
            from_node = row['from']
            to_node = row['to']
            distance = float(row['distance_km'])
            g.add_edge(from_node, to_node, weight=distance)

    return g

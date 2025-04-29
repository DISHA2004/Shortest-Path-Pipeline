import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_with_path(g , path= None):
    pos=nx.spring_layout(g, seed=42)
    edge_labels= nx.get_edge_attributes(g, 'weight')

    # to draw allthe adges and nodes
    nx.draw(g, pos, with_labels=True, node_color='skyblue', node_size=1000,  font_weight='bold')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    # to highlight the result path
    if path and len(path) > 1:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='red', width=3)
        nx.draw_networkx_nodes(g, pos, nodelist=path, node_color='orange')

    plt.title("Warehouse Delivery Network with Shortest Path")
    plt.show()
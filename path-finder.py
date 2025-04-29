from src.ingest import load_graph_csv
from src.visualize import draw_graph_with_path
from src.bfs_path import bfs_shortest_path


if __name__ == "__main__":
    file_path = 'data/sample_delivery_routes.csv'
    graph = load_graph_csv(file_path)
    print("Available warehouse nodes:", ", ".join(graph.nodes()))
    start = input("Enter starting warehouse (e.g., W1): ").strip().upper()
    end = input("Enter destination warehouse (e.g., W6): ").strip().upper()
    if start not in graph or end not in graph:
        print("Invalid warehouse names.")
    else:
        path = bfs_shortest_path(graph, start, end)

        if path:
            total_distance = 0
            for i in range(len(path) - 1):
                edge_data = graph.get_edge_data(path[i], path[i+1])
                total_distance += edge_data['weight']

            print(f"\n Shortest path from {start} to {end}: {' → '.join(path)}")
            print(f" Total distance: {total_distance:.2f} km")

             # Visualize the graph and the path
            draw_graph_with_path(graph, path)
        else:
            print(" No path found.")

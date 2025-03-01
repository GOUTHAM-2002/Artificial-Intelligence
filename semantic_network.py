"1956 - Semantic Network Graph (Directed Graph)"

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes (concepts)
concepts = ["Car", "Vehicle", "Wheel", "Fuel", "Engine", "Transportation"]
G.add_nodes_from(concepts)

# Add edges (relationships)
relationships = [
    ("Car", "Vehicle", "is a"),
    ("Car", "Wheel", "has"),
    ("Car", "Engine", "has"),
    ("Car", "Fuel", "needs"),
    ("Vehicle", "Transportation", "is type of"),
    ("Vehicle", "Fuel", "needs")
]

for source, target, relation in relationships:
    G.add_edge(source, target, relation=relation)

def find_relation(G, source, target):
    """Find direct relation between two concepts"""
    for u, v, data in G.edges(data=True):
        if u == source and v == target:
            return f"{source} {data['relation']} {target}"
    return "No direct relation found"

def infer_relation(G, source, target, visited=None):
    """Infer indirect relations between concepts using path traversal"""
    if visited is None:
        visited = set()
    
    if source == target:
        return []
    
    visited.add(source)
    paths = []
    
    for neighbor in G.neighbors(source):
        if neighbor not in visited:
            relation = G[source][neighbor]['relation']
            if neighbor == target:
                paths.append([(source, neighbor, relation)])
            else:
                sub_paths = infer_relation(G, neighbor, target, visited.copy())
                for path in sub_paths:
                    paths.append([(source, neighbor, relation)] + path)
    
    return paths

def visualize_network(G):
    """Visualize the semantic network"""
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=2000, alpha=0.7)
    nx.draw_networkx_labels(G, pos)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
    
    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Semantic Network")
    plt.axis('off')
    plt.show()

# Example usage
print("\nDirect Relations:")
print(find_relation(G, "Car", "Vehicle"))
print(find_relation(G, "Car", "Fuel"))

print("\nInferred Relations:")
paths = infer_relation(G, "Car", "Transportation")
for path in paths:
    inference = " -> ".join([f"{source} {relation} {target}" 
                            for source, target, relation in path])
    print(inference)

# Visualize the network
visualize_network(G)
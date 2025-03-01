"""
DENDRAL (1965) - First Expert System for Chemical Structure Elucidation
--------------------------------------------------------------------
Developed at Stanford University by Edward Feigenbaum, Bruce Buchanan, 
Joshua Lederberg, and Carl Djerassi

Historical Significance:
- One of the first expert systems in artificial intelligence
- Pioneered the use of heuristic rules in scientific reasoning
- Helped chemists identify unknown organic molecules
- Demonstrated how computers could emulate expert decision-making

This simulation demonstrates:
1. Generation of possible molecular structures
2. Application of chemical valency rules
3. Structure visualization
4. Basic chemical constraint satisfaction
"""

import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations
import random

# Enhanced chemical rules
chemical_rules = {
    "C": {
        "valency": 4,
        "color": "#333333",  # Dark gray for Carbon
        "size": 1000
    },
    "H": {
        "valency": 1,
        "color": "#0088FF",  # Blue for Hydrogen
        "size": 700
    },
    "O": {
        "valency": 2,
        "color": "#FF0000",  # Red for Oxygen
        "size": 900
    },
    "N": {
        "valency": 3,
        "color": "#00FF00",  # Green for Nitrogen
        "size": 900
    }
}

def generate_structures(formula):
    """Generate all possible molecular structures"""
    atoms = list(formula)
    structures = set(permutations(atoms))
    return ["-".join(structure) for structure in structures]

def filter_valid_structures(structures):
    """Filter structures based on chemical rules"""
    valid_structures = []
    for structure in structures:
        atoms = structure.split("-")
        atom_counts = {atom: atoms.count(atom) for atom in set(atoms)}
        
        # Enhanced validation with proper chemical rules
        total_valency = sum(atom_counts[atom] * chemical_rules[atom]["valency"] 
                           for atom in atom_counts if atom in chemical_rules)
        
        if total_valency % 2 == 0:  # Valid molecules have even total valency
            valid_structures.append(structure)
    
    return valid_structures

def visualize_molecule(structure):
    """Visualize molecular structure using NetworkX and Matplotlib"""
    try:
        G = nx.Graph()
        atoms = structure.split("-")
        
        # Create nodes (atoms)
        for i, atom in enumerate(atoms):
            if atom not in chemical_rules:
                raise ValueError(f"Unknown atom type: {atom}")
            G.add_node(i, element=atom)
        
        # Create edges (bonds) based on valency rules
        available_valency = {i: chemical_rules[atoms[i]]["valency"] 
                           for i in range(len(atoms))}
        
        # Connect atoms based on available valency
        for i in range(len(atoms)):
            for j in range(i + 1, len(atoms)):
                if available_valency[i] > 0 and available_valency[j] > 0:
                    G.add_edge(i, j)
                    available_valency[i] -= 1
                    available_valency[j] -= 1

        plt.clf()  # Clear the current figure
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G, k=1, iterations=50)  # Adjust layout parameters
        
        # Draw nodes (atoms)
        for element in chemical_rules:
            node_list = [n for n, attr in G.nodes(data=True) 
                        if attr["element"] == element]
            if node_list:  # Only draw if there are nodes of this element
                nx.draw_networkx_nodes(G, pos,
                                     nodelist=node_list,
                                     node_color=chemical_rules[element]["color"],
                                     node_size=chemical_rules[element]["size"])
        
        # Draw edges (bonds)
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
        
        # Add labels
        labels = {n: attr["element"] for n, attr in G.nodes(data=True)}
        nx.draw_networkx_labels(G, pos, labels, font_size=12, font_weight='bold')
        
        plt.title(f"Molecular Structure: {structure}")
        plt.axis('off')
        plt.tight_layout()
        return True
    except Exception as e:
        print(f"⚠️ Visualization error: {str(e)}")
        return False

def analyze_molecule(formula):
    """Analyze and visualize molecular structures"""
    print(f"🧪 Analyzing molecular formula: {formula}")
    
    try:
        generated = generate_structures(formula)
        valid = filter_valid_structures(generated)
        
        print(f"\n📊 Analysis Results:")
        print(f"- Total possible structures: {len(generated)}")
        print(f"- Valid structures: {len(valid)}")
        
        if valid:
            print("\n🔍 Sample valid structures:")
            for i, structure in enumerate(valid[:3], 1):
                print(f"{i}. {structure}")
            
            # Visualize a random valid structure
            sample_structure = random.choice(valid)
            if visualize_molecule(sample_structure):
                plt.show(block=True)  # Make sure plot is shown and blocks
                plt.close()  # Close the plot after showing
        else:
            print("\n⚠️ No valid structures found!")
    except Exception as e:
        print(f"⚠️ Analysis error: {str(e)}")

# Example usage
if __name__ == "__main__":
    formulas = ["CH4", "C2H6O", "C3H8O"]
    
    print("🧬 DENDRAL Structure Analysis System")
    print("-----------------------------------")
    
    for formula in formulas:
        analyze_molecule(formula)
        print("\n" + "="*50 + "\n")
        plt.close('all')  # Close all figures after each analysis
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(n: int, p: float) -> nx.Graph:
    return nx.gnp_random_graph(n, p)

def degree_based_matching_desc(G: nx.Graph) -> set:
    matching = set()
    sorted_nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)
    matched = set()
    for u, _ in sorted_nodes:
        if u in matched:
            continue
        for v in G.neighbors(u):
            if v not in matched:
                matching.add((u, v))
                matched.add(u)
                matched.add(v)
                break
    return matching

def degree_based_matching_asc(G: nx.Graph) -> set:
    matching = set()
    sorted_nodes = sorted(G.degree, key=lambda x: x[1])
    matched = set()
    for u, _ in sorted_nodes:
        if u in matched:
            continue
        for v in G.neighbors(u):
            if v not in matched:
                matching.add((u, v))
                matched.add(u)
                matched.add(v)
                break
    return matching

def main():
    # Generate a random graph
    n = 120
    p = 0.04
    G = generate_random_graph(n, p)
    
    # Test the heuristics
    matching_desc = degree_based_matching_desc(G)
    matching_asc = degree_based_matching_asc(G)

    # Output results
    print("Matching by descending degree:", len(matching_desc))
    print("Matching by ascending degree:", len(matching_asc))
    
    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for the nodes
    nx.draw(G, pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()

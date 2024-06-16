import networkx as nx
import time
import numpy as np

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

def verify_matching(G, matching):
    nodes = set()
    for u, v in matching:
        if u in nodes or v in nodes:
            return False
        nodes.add(u)
        nodes.add(v)
    return True

def compare_heuristics(G, trials=100):
    times_desc = []
    times_asc = []
    sizes_desc = []
    sizes_asc = []

    for _ in range(trials):
        start = time.time()
        matching_desc = degree_based_matching_desc(G)
        times_desc.append(time.time() - start)
        sizes_desc.append(len(matching_desc))

        start = time.time()
        matching_asc = degree_based_matching_asc(G)
        times_asc.append(time.time() - start)
        sizes_asc.append(len(matching_asc))

    print("Average size (desc):", np.mean(sizes_desc))
    print("Average time (desc):", np.mean(times_desc))
    print("Average size (asc):", np.mean(sizes_asc))
    print("Average time (asc):", np.mean(times_asc))

def main():
    # Generate a random graph
    n = 120
    p = 0.04
    G = generate_random_graph(n, p)
    
    # Compare heuristics
    compare_heuristics(G)

if __name__ == "__main__":
    main()

from bellman_ford import Graph
if __name__ == "__main__":
    g = Graph(4)

    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, 5)
    g.add_edge(2, 0, -6)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, -2)


    print(g.bellman_ford(0))
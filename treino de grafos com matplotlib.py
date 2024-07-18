import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5])

edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (1, 5)]
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12, font_weight='bold', pos=nx.spring_layout(G))
plt.title("Exemplo de Grafo não Direcionado")
plt.show()
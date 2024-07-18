import networkx as nx
import matplotlib.pyplot as plt

G_conexo = nx.Graph()
edges_conexo = [(1, 2), (2, 3), (3, 4), (4, 1), (3, 5), (5, 6)]
G_conexo.add_edges_from(edges_conexo)

G_disco = nx.Graph()
edges_disco = [(1, 2), (2, 3), (3, 4), (4, 1), (5, 6)]
G_disco.add_edges_from(edges_disco)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
nx.draw(G_conexo, with_labels=True, node_color="lightblue", node_size=1500, font_size=12, font_weight='bold')
plt.title("Conexo")

plt.subplot(1, 2, 2)
nx.draw(G_disco, with_labels=True, node_color='lightcoral', node_size=1500, font_size=12, font_weight='bold')
plt.title("Disconexo")

plt.tight_layout()
plt.show()
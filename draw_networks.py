import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

node_num = 150

G = nx.random_geometric_graph(node_num, 0.15)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, "pos")

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center

anchor_ids = []
anchor_ids.append(50)

p_1 = dict(nx.single_source_shortest_path_length(G, anchor_ids[0]))

for k, v in p_1.items():
    if p_1[k] > 1:
        anchor_ids.append(k)
        break

p_2 = dict(nx.single_source_shortest_path_length(G, anchor_ids[1]))

color_s = []

for i in range(node_num):
    if p_1[i] == 0 or p_2[i] == 0:
        color_s.append('red')
    elif p_1[i] <= 2 or p_2[i] <= 2:
        color_s.append('gold')
    else:
        color_s.append('skyblue')



node_s = []
for i in range(node_num):
    node_s.append(300)


plt.figure(figsize=(8, 8))
nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=list(range(node_num)),
    node_size=node_s,
    node_color=color_s,
    # cmap=plt.cm.Reds_r,
)

plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.axis("off")
plt.savefig('tmp.png', dpi=200, bbox_inches='tight')
plt.show()

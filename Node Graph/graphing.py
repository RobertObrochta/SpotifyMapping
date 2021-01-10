
import main as sp
from main import client_id, client_secret
import networkx as nx
import matplotlib.pyplot as plt


names = sp.SpotifyAPI(client_id, client_secret).artist_track_name()
G = nx.Graph()

options = {
    'node_color' : '#26E07C',
    'edge_color' : '#2F566C',
    'width' : 3,
    'with_labels' : True,
}

# adds nodes from the list of names, returned in artist_track_name() function
G.add_nodes_from(names)

# this ensures that the range of r is within the bounds of the indices in 'names'
# adds the connections between the nodes
for i in range(len(names)):
    r = i + 1
    if r < 50:
        G.add_edges_from([(names[i], names[r])])

pos = nx.spring_layout(G)

nx.draw(G, pos, **options)
plt.show()

import main as sp
from main import client_id, client_secret
import networkx as nx
import matplotlib.pyplot as plt

# keep reworking, fit labels into graph, and space them out (if I can)
# look at possible options for drawing the graph 
G = nx.star_graph(1)

options = {
    'node_color' : '#26E07C',
    'edge_color' : '#26E07C',
    'width' : 13,
    'with_labels' : True,
}

names = sp.SpotifyAPI(client_id, client_secret).artist_track_name()

# adds nodes from the list of names, returned in artist_track_name() function
G.add_nodes_from(names)
pos = nx.spring_layout(G)

nx.draw(G, pos, **options)
plt.show()
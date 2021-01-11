import freq as fr
from freq import client_id, client_secret
import matplotlib.pyplot as plt

names = fr.SpotifyAPI(client_id, client_secret).artist_track_name()


plt.bar(range(len(names)), list(names.values()), align='center')
plt.xticks(range(len(names)), list(names.keys()))
plt.show()
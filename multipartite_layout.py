import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

edge1 = pd.read_csv('edge1.csv')
node1 = pd.read_csv('node1_copy.csv')
subset_color = {
    "business strat": "gold",
    "business obj": "violet",
    "sec control": "limegreen",

}


# build graph:
G = nx.from_pandas_edgelist(edge1, 'Source', 'Target', [
                            'Source', 'Target', 'TransactionAmt', 'Date'], create_using=nx.MultiDiGraph())
nx.set_node_attributes(G, node1.set_index('Account')[
                       'CustomerName'].to_dict(), 'CustomerName')
nx.set_node_attributes(G, node1.set_index('Account')['Type'].to_dict(), 'Type')
nx.set_node_attributes(G, node1.set_index('Account')
                       ['layer'].to_dict(), 'layer')
color = [subset_color[data['layer']] for v, data in G.nodes(data=True)]


# plot graph
pos = nx.multipartite_layout(G, subset_key="layer",)
plt.figure(figsize=(20, 8))
nx.draw(G, pos, node_color=color, with_labels=True)
plt.axis("auto")
plt.show()

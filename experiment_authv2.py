import csv
from re import L
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
 
# class Node:
#   def __init__(self, source, computer):
#     self.source = source
#     self.computer = computer

# opening the CSV file
G = nx.Graph()
with open('auth_1_12.csv', mode ='r')as file:
  for line in file:
    split_line = line.split(',')
    source_node = (split_line[1], split_line[3])
    destination_node = (split_line[2], split_line[4])
    G.add_nodes_from([source_node, destination_node])
    G.add_edge(source_node, destination_node)

# for edge in G.edges:
#     print(edge)

# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
node2vec = Node2Vec(G, dimensions=20, walk_length=16, num_walks=100)
model = node2vec.fit(window=10, min_count=1)

for node, _ in model.most_similar(('C1035$@DOM1','C1035')):
    print(node)
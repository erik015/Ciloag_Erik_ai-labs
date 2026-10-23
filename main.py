import math

import numpy as np
from scipy.special import softmax as smax
from math import exp
from Node import Node
import random

# ex. 1
print("ex. 1")


def softmax(list1):
    result = []
    sum_exp = sum([exp(x) for x in list1])
    for i in list1:
        result.append(exp(i) / sum_exp)
    return result


a = [-0.4, 0, 0.2, 0.2, 0.4]
print("Implemented softmax: ", softmax(a))
print("Scipy softmax: ", smax(a), "\n")

# ex. 3
print("ex. 3")


def print_graph(nodes):
    for node in nodes:
        for neighbour in node.neighbours:
            print(f"{node} -> {neighbour}")


f = open("graph1.txt", "r")
nr_vertices = int(f.readline())

nodes = []
for i in range(1, nr_vertices + 1):
    nodes.append(Node(i))

line = f.readline()
while line:
    list1 = line.split()
    nodes[int(list1[0]) - 1].edge(nodes[int(list1[1]) - 1])
    line = f.readline()

f.close()
print_graph(nodes)

node_out_degree = max(nodes, key=lambda node: node.out_degree())
print(f"\nThe vertex with the highest out-degree: {node_out_degree}\n")

new_nr_vertices = int(0.6 * nr_vertices)
new_nodes = random.sample(nodes, new_nr_vertices)

for node in new_nodes:
    new_nr_edges = int(0.8 * len(node.neighbours))
    new_neighbours = random.sample(node.neighbours, new_nr_edges)
    node.neighbours = new_neighbours

print(f"The number of subgraph's vertices: {new_nr_vertices}")
print_graph(new_nodes)


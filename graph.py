import json
import networkx as nx
import matplotlib.pyplot as plt


class graph:
    edge = []

    def __init__(self):
        self.nodes = 0

    def readFromFile(self, file='test.in'):
        with open(file, 'r') as F:
            self.nodes = int(F.readline())

            for X in range(0, self.nodes + 1):
                self.edge.append(' ')

            for X in F.read().splitlines():
                self.edge[int(X.split(' ')[0])] += X.split(' ')[1] + ' '

    def readFromJson(self, input='test.json'):
        if '.json' in input:
            with open(input, 'r') as F:
                X = json.loads(F.read())
        else:
            X = json.loads(input)
        self.nodes = int(X['nodes'])

        for Z in range(0, self.nodes + 1):
            self.edge.append(' ')

        for Z in X['edges']:
            self.edge[int(Z['node'])] += Z['edge'] + ' '

    def display(self):
        G = nx.DiGraph()

        for X in range(1, self.nodes + 1):
            G.add_node(X)

            for Y in self.edge[X].strip(' ').split(' '):
                if Y.isdigit():
                    G.add_edge(X, int(Y))

        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='orange', arrowsize=20)

        plt.gcf().canvas.set_window_title('Graph')
        plt.show()

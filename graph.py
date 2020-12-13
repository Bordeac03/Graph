import json
import networkx as nx
import matplotlib.pyplot as plt


class graph:
    edge = []

    def __init__(self):
        self.nodes = 0

    def __createGraph(self):
        plt.clf()
        self.G = nx.DiGraph()
        for X in range(1, self.nodes + 1):
            self.G.add_node(X)

            for Y in self.edge[X].strip(' ').split(' '):
                if Y.isdigit():
                    self.G.add_edge(X, int(Y), length=5)

        self.pos = nx.circular_layout(self.G)
        nx.draw(self.G, self.pos, with_labels=True, node_color='orange', edge_color='orange', arrowsize=20)

    def readFromFile(self, file='test.in'):
        with open(file, 'r') as F:
            self.nodes = int(F.readline())

            for X in range(0, self.nodes + 1):
                self.edge.append(' ')

            for X in F.read().splitlines():
                self.edge[int(X.split(' ')[0])] += X.split(' ')[1] + ' '

        self.__createGraph()

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

        self.__createGraph()

    def addNode(self, neighbours=''):
        self.nodes += 1
        self.edge.append(' ' + neighbours + ' ')
        self.__createGraph()

    def addNodes(self, nodes=0, neighbours=None):
        self.nodes += nodes
        for X in range(nodes):
            self.edge.append(' ' + neighbours[X] + ' ')
        self.__createGraph()

    def addEdge(self, X=0, Y=0):
        if X <= self.nodes and Y <= self.nodes:
            self.edge[X] += str(Y) + ' '
        else:
            print('Nodul nu exista')
        self.__createGraph()

    def display(self):
        plt.gcf().canvas.set_window_title('Graph')
        plt.show()

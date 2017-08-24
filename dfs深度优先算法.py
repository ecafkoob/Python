#!/usr/bin/python
# -*- coding: utf-8 -*-


class Graph(object):
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if (u != v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self, root=None):
        orderdfs = []

        def dfs(node):
            self.visited[node] = True
            orderdfs.append(node)
            for n in self.node_neighbors[node]:
                if n not in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        for node in self.nodes():
            if node not in self.visited:
                dfs(node)

        print(orderdfs)
        return orderdfs

    def breadth_first_search(self, root=None):
        queue = []
        orderbfs = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)

                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (n not in self.visited) and (n not in queue):
                        queue.append(n)
                        orderbfs.append(n)

        if root:
            queue.append(root)
            orderbfs.append(root)
            bfs()

        for node in self.nodes():
            if node not in self.visited:
                queue.append(node)
                orderbfs.append(node)
                bfs()
        print(orderbfs)

        return orderbfs


if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i + 1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print("nodes:", g.nodes())

    orderbfs = g.breadth_first_search(1)
    orderdfs = g.depth_first_search(1)


class Node:

    def __init__(self, x, y, t):
        self.neighbors = []
        self.prev = None
        self.type = t
        self.dist = float('inf')
        self.xy = (x, y)

    def __repr__(self):
        return self.xy.__str__()

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def find_path(nodes, source, target):

    source.dist = 0

    while nodes:
        curr = nodes[0]
        for i in nodes:
            if i.dist < curr.dist:
                curr = i

        nodes.remove(curr)
        if curr == target:
            return target

        for n in curr.neighbors:
            alt = curr.dist + 1
            if alt < n.dist:
                n.dist = alt
                n.prev = curr
    return None

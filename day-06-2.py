from collections import deque
from sys import stdin

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.descendents = []
        self.prev = None
        self.depth = 0

def main():
    nodes = {"COM": Node("COM")}
    for line in stdin:
        n1, n2 = line.rstrip().split(')')
        if n1 not in nodes:
            nodes[n1] = Node(n1)
        if n2 not in nodes:
            nodes[n2] = Node(n2)
        nodes[n1].children.append(nodes[n2])
        nodes[n2].prev = nodes[n1]
        nodes[n2].depth = nodes[n1].depth + 1
    trace_ancestors(nodes["YOU"])
    trace_ancestors(nodes["SAN"])
    bfs(nodes["COM"])
    root_depth = max(nodes[node].depth for node in nodes if len(nodes[node].descendents) == 2)
    print(nodes["YOU"].depth + nodes["SAN"].depth - 2 * root_depth - 2)

def bfs(node):
    q = deque([node])
    while q:
        current = q.popleft()
        if current.prev:
            current.depth = current.prev.depth + 1
        for c in current.children:
            q.append(c)

def trace_ancestors(node):
    name = node.name
    while node.prev:
        node.prev.descendents.append(name)
        node = node.prev

if __name__ == "__main__":
    main()

from sys import stdin

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def main():
    nodes = {"COM": Node("COM")}
    for line in stdin:
        n1, n2 = line.rstrip().split(')')
        if n1 not in nodes:
            nodes[n1] = Node(n1)
        if n2 not in nodes:
            nodes[n2] = Node(n2)
        nodes[n1].children.append(nodes[n2])
    print(dfs(nodes["COM"], 0))

def dfs(node, depth):
    if len(node.children) == 0:
        return depth
    return depth + sum([dfs(c, depth + 1) for c in node.children])

if __name__ == "__main__":
    main()

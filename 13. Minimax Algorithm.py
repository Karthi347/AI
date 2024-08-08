import math

class Node:
    def __init__(self, value, depth, is_maximizing):
        self.value, self.depth, self.is_maximizing = value, depth, is_maximizing
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def minimax(node, alpha, beta):
    if node.depth == 0 or not node.children:
        return node.value
    best_value = -math.inf if node.is_maximizing else math.inf
    for child in node.children:
        child_value = minimax(child, alpha, beta)
        if node.is_maximizing:
            best_value = max(best_value, child_value)
            alpha = max(alpha, best_value)
        else:
            best_value = min(best_value, child_value)
            beta = min(beta, best_value)
        if beta <= alpha: break
    return best_value

def create_game_tree():
    nodes = [Node(i * 10, 1, True) for i in range(1, 7)]
    root = Node(0, 3, True)
    for i in range(3):
        child = Node(0, 2, False)
        child.add_child(nodes[2 * i])
        child.add_child(nodes[2 * i + 1])
        root.add_child(child)
    return root

print("Best value:", minimax(create_game_tree(), -math.inf, math.inf))

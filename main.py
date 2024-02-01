import random


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def min_value_node(node):
    #В бінарному дереві пошуку найменший елемент завжди найлівіший
    current = node
    while current.left:
        current = current.left
    return current.val


def max_value_node(node: Node):
    #В бінарному дереві пошуку найбільший елемент завжди нвйправіший
    current = node
    while current.right:
        current = current.right
    return current.val


def sum_values_recursive(root: Node) -> int:
    if root is None:
        return 0
    return root.val + sum_values_iterable(root.left) + sum_values_iterable(root.right)


def sum_values_iterable(node: Node) -> int:
    if node is None:
        return 0

    values_sum = 0

    stack = [node]

    while len(stack) > 0:
        current_node = stack.pop()
        values_sum += current_node.val

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return values_sum


if __name__ == "__main__":
    tree = Node(random.randint(10, 1000))

    for _ in range(100):
        tree = insert(tree, random.randint(10, 1000))

    print("Завдання 1:", end='\n')
    print(f"Min value: {min_value_node(tree).val}", end='\n\n')

    print("Завдання 2:", end='\n')
    print(f"Max value: {max_value_node(tree).val}", end='\n\n')

    print("Завдання 3:", end='\n')
    print(f"Sum values (iterable): {sum_values_iterable(tree)}", end='\n')
    print(f"Sum values (recursive): {sum_values_recursive(tree)}", end='\n')

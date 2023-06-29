class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")

    def print_leaves(self):
        self._print_leaves_recursive(self.root)

    def _print_leaves_recursive(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            self._print_leaves_recursive(node.left)
            self._print_leaves_recursive(node.right)

    def bfs(self):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        self._dfs_recursive(self.root)

    def _dfs_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._dfs_recursive(node.left)
            self._dfs_recursive(node.right)

    def sum_left_leaves(self):
        return self._sum_left_leaves_recursive(self.root, False)

    def _sum_left_leaves_recursive(self, node, is_left):
        if node is None:
            return 0

        if node.left is None and node.right is None and is_left:
            return node.data

        left_sum = self._sum_left_leaves_recursive(node.left, True)
        right_sum = self._sum_left_leaves_recursive(node.right, False)

        return left_sum + right_sum

    def sum_all_nodes(self):
        return self._sum_all_nodes_recursive(self.root)

    def _sum_all_nodes_recursive(self, node):
        if node is None:
            return 0

        left_sum = self._sum_all_nodes_recursive(node.left)
        right_sum = self._sum_all_nodes_recursive(node.right)

        return node.data + left_sum + right_sum

    def count_subtrees_with_sum(self, target_sum):
        count = [0]  # Using a list to store the count since integer is immutable

        self._count_subtrees_recursive(self.root, target_sum, count)

        return count[0]

    def _count_subtrees_recursive(self, node, target_sum, count):
        if node is None:
            return 0

        left_sum = self._count_subtrees_recursive(node.left, target_sum, count)
        right_sum = self._count_subtrees_recursive(node.right, target_sum, count)
        total_sum = left_sum + right_sum + node.data

        if total_sum == target_sum:
            count[0] += 1

        return total_sum

    def maximum_level_sum(self):
        if self.root is None:
            return 0

        max_sum = float("-inf")
        queue = []
        queue.append(self.root)

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0)
                level_sum += node.data

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            max_sum = max(max_sum, level_sum)

        return max_sum

    def print_odd_level_nodes(self):
        self._print_odd_level_nodes_recursive(self.root, 1)

    def _print_odd_level_nodes_recursive(self, node, level):
        if node is None:
            return

        if level % 2 == 1:
            print(node.data, end=" ")

        self._print_odd_level_nodes_recursive(node.left, level + 1)
        self._print_odd_level_nodes_recursive(node.right, level + 1)


# Usage example
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(9)

print("Height of the tree:", tree.height())

print("Preorder traversal:")
tree.preorder_traversal()
print()

print("Inorder traversal:")
tree.inorder_traversal()
print()

print("Postorder traversal:")
tree.postorder_traversal()
print()

print("Leaves of the tree:")
tree.print_leaves()
print()

print("BFS traversal:")
tree.bfs()
print()

print("DFS traversal:")
tree.dfs()
print()

print("Sum of left leaves:", tree.sum_left_leaves())

print("Sum of all nodes:", tree.sum_all_nodes())

target_sum = 10
count = tree.count_subtrees_with_sum(target_sum)
print(f"Number of subtrees with sum {target_sum}: {count}")

print("Maximum level sum:", tree.maximum_level_sum())

print("Nodes at odd levels:")
tree.print_odd_level_nodes()
print()
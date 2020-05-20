class Bst:

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.insert_node(self.root, key, value)

    def insert_node(self, node, key, value):

        if not node:
            node = Node(key, value)
            return node

        if key < node.key:
            node.left = self.insert_node(node.left, key, value)
        elif key > node.key:
            node.right = self.insert_node(node.right, key, value)

        return node

    def get(self, key):

        node = self.get_node(self.root, key)
        if not node:
            return None
        else:
            return node.value

    def min(self):
        return self.get_min(self.root)

    def get_min(self, node):
        if not node.left:
            return node
        else:
            min = self.get_min(node.left)

        return min

    def get_node(self, node, key):
        if not node or node.key == key:
            return node
        elif key < node.key:
            node = self.get_node(node.left, key)
        elif key > node.key:
            node = self.get_node(node.right, key)

        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, node, key):

        # base case
        if not node:
            return node
        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)

        else:
            if not node.left and not node.right:
                node = None

            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left

            else:
                min_node = self.get_min(node.right)
                node.key = min_node.key
                node.value = min_node.value

                node.right = self.delete_node(node.right, node.key)
        return node

    def in_order_traversal(self):

        self.i_o_t(self.root)

    def i_o_t(self, node):
        if node:
            self.i_o_t(node.left)
            print(node.key)
            self.i_o_t(node.right)

    def pre_order_traversal(self):

        self.pre_o_t(self.root)

    def pre_o_t(self, node):
        if node:
            print(node.key)
            self.pre_o_t(node.left)
            self.pre_o_t(node.right)

    def post_order_traversal(self):

        self.post_o_t(self.root)

    def post_o_t(self, node):
        if node:
            self.post_o_t(node.left)
            self.post_o_t(node.right)
            print(node.key)

    def convert_sorted_array(self, array):
        if not array:
            return None

        mid = int(len(array) / 2)

        node = Node(None, array[mid])
        node.left = self.convert_sorted_array(array[:mid])
        node.right = self.convert_sorted_array(array[mid+1:])

        return node

    def c_s_a(self,array):
        if not array:
            return []



class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

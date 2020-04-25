class LinkedList:

    def __init__(self):
        self.head = None

    def add_back(self, value):

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def add_front(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        temp_node = self.head

        self.head = new_node
        new_node.next = temp_node
        return

    def get_first(self):
        return self.head.value

    def get_last(self):

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node.value

    def delete(self, value):
        if not self.head:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return
        current_node = self.head

        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            else:
                current_node = current_node.next

    def size(self):
        size = 1

        if not self.head:
            return 0

        current_node = self.head

        while current_node.next:
            size += 1
            current_node = current_node.next

        return size

    def reverse(self):
        if not self.head.next:
            return
        current_node = prev = self.head
        current_node = current_node.next
        prev.next = None
        while current_node.next:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp

        current_node.next = prev
        self.head = current_node

    def reverse_list(self, l):
        if not l:
            return
        current_node = prev = l
        current_node = current_node.next
        prev.next = None
        while current_node.next:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp

        current_node.next = prev
        l = current_node
        return l

    def merge_list(self, h2):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = h2.head

    def sort(self):
        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.value > q.value:
                    p.value, q.value = q.value, p.value
                p = p.next
            end = p

    def is_palindrome(self):
        cp_linked = self.copy_list(self.head)
        c = self.reverse_list(cp_linked)
        current_node = self.head

        while current_node.next:
            if c.value != current_node.value:
                return False
            c = c.next
            current_node = current_node.next

        return True

    def copy(self):
        current_node = self.head.next
        cp = Node(self.head.value)
        cpt = cp
        while current_node:
            temp = Node(current_node.value)
            cpt.next = temp
            cpt = cpt.next
            current_node = current_node.next

        return cp

    def copy_list(self, l):
        current_node = l
        cp = Node(l.value)
        cpt = cp
        while current_node:
            temp = Node(current_node.value)
            cpt.next = temp
            cpt = cpt.next
            current_node = current_node.next

        return cp

    def __str__(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                print("{} =>".format(current_node.value), end=" ")
            else:
                print("{}".format(current_node.value), end=" ")
            current_node = current_node.next
        return ""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

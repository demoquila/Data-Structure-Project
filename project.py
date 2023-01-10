import time
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next
        self.left = None
        self.right = None


# Complete Binary Tree based on singly linked list


class CompleteBinaryTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def get_node(self, i):
        """Returns the node at index i."""
        current_node = self.root
        for m in range(i):
            current_node = current_node.next
        return current_node

    def parent(self, i):
        """Returns the parent of the node at index i."""
        if i == 0:
            return None
        return self.get_node((i - 1) // 2)

    def left_child(self, i):
        """Returns the left child of the node at index i."""
        left = 2 * i + 1
        if left >= self.size():
            return None
        return self.get_node(left)

    def right_child(self, i):
        """Returns the right child of the node at index i."""
        right = 2 * i + 2
        if right >= self.size():
            return None
        return self.get_node(right)

    def size(self):
        """Returns the number of nodes in the tree."""
        current_node = self.root
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def append(self, key):
        """Appends a new node with the given key to the end of the list."""
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if current.left is None:
                    current.left = node
                    break
                elif current.right is None:
                    current.right = node
                    break
                else:
                    current = current.left
        self._size += 1

    def pop(self):
        """Removes and returns the last node in the list."""
        if self.root is None:
            return None
        else:
            current = self.root
            parent = None
            while True:
                if current.right is not None:
                    parent = current
                    current = current.right
                elif current.left is not None:
                    parent = current
                    current = current.left
                else:
                    break
            if parent is None:
                node = self.root
                self.root = None
            elif parent.right == current:
                node = parent.right
                parent.right = None
            else:
                node = parent.left
                parent.left = None
            self._size -= 1
            return node

    def set_node(self, i, key):
        """Sets the node at the given index to the given key."""
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        else:
            current = self.root
            for _ in range(i):
                if i % 2 == 0:
                    current = current.right
                else:
                    current = current.left
            current.key = key


# A test
tree1 = CompleteBinaryTree()

# create the nodes and set their links
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

tree1.root = node1

# access the nodes using the tree methods
node_test = tree1.get_node(3)
print(node_test.key)  # should print 4
parent_test = tree1.parent(3)
print(parent_test.key)  # should print 2
left_child1 = tree1.left_child(2)
print(left_child1.key)  # should print 6
right_child1 = tree1.right_child(1)
print(right_child1.key)  # should print 5


class MinPriorityQueue:
    def __init__(self):
        self.tree = CompleteBinaryTree()

    def insert(self, key):
        """Inserts a new node with the given key into the queue."""
        node = Node(key)
        self.tree.append(node)  # append the new node to the end of the list
        self.heapify_up(self.tree.size() - 1)  # restore the min-heap property

    def del_min(self):
        """Removes and returns the node with the minimum key."""
        if self.tree.size() == 0:
            return None
        elif self.tree.size() == 1:
            return self.tree.pop()  # remove the only node in the queue
        else:
            min_node = self.tree.get_node(0)  # get the root node (minimum key)
            last_node = self.tree.pop()  # remove the last node in the list
            self.tree.set_node(0, last_node)  # set the last node as the root
            self.heapify_down(0)  # restore the min-heap property
            return min_node

    def heapify_up(self, i):
        """Restores the min-heap property by bubbling the node at index i up."""
        while i > 0:
            parent_i = (i - 1) // 2
            if self.tree.get_node(i).key < self.tree.get_node(parent_i).key:
                # swap the keys of the nodes
                self.tree.get_node(i).key, self.tree.get_node(parent_i).key = self.tree.get_node(
                    parent_i).key, self.tree.get_node(i).key
                i = parent_i  # update the index to the parent's index
            else:
                break

    def heapify_down(self, i):
        """Restores the min-heap property by bubbling the node at index i down."""
        size = self.tree.size()
        while i < size:
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            min_i = i
            if left_i < size and self.tree.get_node(left_i).key < self.tree.get_node(min_i).key:
                min_i = left_i
            if right_i < size and self.tree.get_node(right_i).key < self.tree.get_node(min_i).key:
                min_i = right_i
            if min_i != i:
                # swap the keys of the nodes
                self.tree.get_node(i).key, self.tree.get_node(min_i).key = self.tree.get_node(
                    min_i).key, self.tree.get_node(i).key
                i = min_i  # update the index to the child's index
            else:
                break


# create a new minimum priority queue
queue = MinPriorityQueue()

# insert some keys
queue.insert(5)
queue.insert(2)
queue.insert(1)
queue.insert(3)
queue.insert(4)

# remove and print the minimum key
print(queue.del_min().key)  # should print 1

print(queue.del_min().key)  # should print 2

print(queue.del_min().key)  # should print 3

print(queue.del_min().key)  # should print  4

print(queue.del_min().key)  # should print 5

# try removing from an empty queue
print(queue.del_min())  # None

# Create an empty minimum priority queue
pq = MinPriorityQueue()

# Perform a series of insert and delMin operations and measure the time taken
times = []
for i in range(10000):
    start = time.perf_counter()
    pq.insert(i)
    end = time.perf_counter()
    times.append(end - start)

# Visualize the results using matplotlib
plt.plot(times)
plt.xlabel('Operation number of Insert')
plt.ylabel('Time (seconds)')
plt.show()

times1 = []
for i in range(10000):
    start1 = time.perf_counter()
    pq.del_min()
    end1 = time.perf_counter()
    times1.append(end1 - start1)
plt.plot(times)
plt.xlabel('Operation number of Delmin')
plt.ylabel('Time (seconds)')
plt.show()

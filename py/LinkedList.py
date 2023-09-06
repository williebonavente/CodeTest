# A simple linked list implementation.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def add_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next is not None:
        current_node = current_node.next
      current_node.next = new_node

  def print_list(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next


linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)

linked_list.print_list()

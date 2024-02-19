class LinkedList:
  def __init__(self):
    self.head = self.tail = None
    self.size = 0

  class Node:
    def __init__(self, value):
      self.prev = self.next = None
      self.data = value
  
  def insert_head(self, value):
    node = self.Node(value)
    node.next = self.head
    if self.head is not None:
      self.head.prev = node
    else:
      self.tail = node
    self.head = node
    self.size += 1

  def remove_head(self):
    if self.head is None:
      return None
    value = self.head.data
    self.head = self.head.next
    if self.head is None:
      self.tail = None
    else:
      self.head.prev = None
    self.size -= 1
    return value
  

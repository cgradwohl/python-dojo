class LinkedList:
  def __init__(self):
    self.head = self.tail = None
  
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = self.prev = None

  def insertHead(self, value):
    node = self.Node(value)
    if self.head is None:
      self.head = self.tail = node
      return True
    node.next = self.head
    self.head.prev = node
    self.head = node
    return True
  
  def removeHead(self):
    if self.head is None:
      return None
    node = self.head
    self.head = self.head.next
    if self.head is not None:
      self.head.prev = None
    else:
      self.tail = None
    # set next and prev pointers of node to be removed to None, to help with garbage collection
    node.next = node.prev = None
    return node.value
  
  def insertTail(self, value):
    node = self.Node(value)
    if self.tail is None:
      self.head = self.tail = node
      return True
    node.prev = self.tail
    self.tail.next = node
    self.tail = node
    return True
  
  def removeTail(self):
    if self.tail is None:
      return None
    node = self.tail
    self.tail = self.tail.prev
    if self.tail is not None:
      self.tail.next = None
    else:
      self.head = None
    # set next and prev pointers of node to be removed to None, to help with garbage collection
    node.next = node.prev = None
    return node.value

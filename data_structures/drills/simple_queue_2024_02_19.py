class Queue:
  def __init__(self):
    self.front = self.back = None

  class Node:
    def __init__(self, value):
      self.prev = self.next = None
      self.value = value

  def enqueue(self, value):
    node = self.Node(value)
    node.prev = self.back
    if self.back != None:
      self.back.next = node
    self.back = node
    if self.front == None:
      self.front = node

  def dequeue(self):
    if self.front == None:
      print("Queue is empty.")
      return None
    node = self.front
    self.front = self.front.next
    if self.front != None:
      self.front.prev = None
    else:
      self.back = None
    node.next = None
    return node.value
  
q = Queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

p = q.front
while p != None:
  print(p.value)
  p = p.next


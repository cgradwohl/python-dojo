# Linked List Implementation

class Queue:
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

  
  def __init__(self):
    self.size = 0
    self.front = None
    self.back = None
  
  def print(self):
    ptr = self.front
    while ptr is not None:
      print(ptr.data)
      ptr = ptr.next


  def enqueue(self, value):
    node = self.Node(value)
    if self.back is None:
      self.front = self.back = node
      self.size += 1
      return
    self.back.next = node
    self.back = node
    self.size += 1
    return

  def dequeue(self):
    if self.front is None:
      return None
    node = self.front
    self.front = self.front.next
    if self.front is None:
      self.back = None
    self.size -= 1
    return node.data

  def peek(self):
    return self.front.data

  def is_empty(self):
    return self.size == 0
    

# MAIN
def main():
  my_queue = Queue()
  
  my_queue.enqueue(1)
  my_queue.enqueue(2)
  my_queue.enqueue(3)
  my_queue.enqueue(4)
  my_queue.enqueue(5)
  
  my_queue.print() # 1 2 3 4 5

  print(my_queue.dequeue()) # 1
  print(my_queue.dequeue()) # 2
  print(my_queue.dequeue()) # 3

  print(my_queue.is_empty()) # False
  print(my_queue.peek()) # 4

  print(my_queue.dequeue()) # 4 
  print(my_queue.dequeue()) # 5
  print(my_queue.dequeue()) # None
  print(my_queue.is_empty()) # True



main()

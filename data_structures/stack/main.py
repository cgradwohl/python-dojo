# Implement a Stack data structure. Assume no size constraint.
class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, item):
    # no size constraint, so not checking for overflow
    self.stack.append(item)
  
  def pop(self):
    # check for underflow
    if self.is_empty():
      return Exception("stack is empty.")
    return self.stack.pop()
  
  def is_empty(self):
    return len(self.stack) == 0
  
  def peek(self):
    # check for underflow
    if self.is_empty():
      return Exception("stack is empty.")
    return self.stack[len(self.stack) - 1]
  

# Implement a Stack data structure with an explicit size constraint.
class StackWithSize:
  def __init__(self, size):
    self.stack = [None] * size
    self.top = -1

  def push(self, item):
    # check for overflow
    if self.top == len(self.stack) - 1:
      return Exception("the stack is full")
    self.top += 1
    self.stack[self.top] = item
  
  def pop(self):
    # check for underflow
    if self.is_empty():
      return Exception("stack is empty.")
    item = self.stack[self.top]
    self.stack[self.top] = None
    self.top -= 1
    
    return item
  
  def is_empty(self):
    return self.top == -1
  
  def peek(self):
    # check for underflow
    if self.is_empty():
      return Exception("stack is empty.")
    
    return self.stack[self.top]

# Implement a Stack data structure using a linked list
class StackWithLinkedList:
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

  def __init__(self):
    self.top = None

  def push(self, item):
    node = self.Node(item)
    node.next = self.top
    self.top = node

  def pop(self):
    # check for underflow
    if self.top is None:
      return Exception("stack is empty.")
    data = self.top.data
    self.top = self.top.next

    return data
  
  def peek(self):
    if self.top is None:
      return Exception("stack is empty")
    return self.top.data
  
  def is_empty(self):
    return self.top is None
  

def main():
  stack = Stack()
  stack.push(4)
  stack.push(2)
  stack.push(1)
  stack.push(7)
  stack.push(5)

  print(stack.pop()) # 5
  print(stack.pop()) # 7
  print(stack.pop()) # 1
  print(stack.pop()) # 2
  print(stack.peak()) # 4
  print(stack.is_empty()) # False
  print(stack.pop()) # 4
  print(stack.pop()) # stack is empty.

main()

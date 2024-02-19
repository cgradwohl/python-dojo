class MonotonicStack:
  def __init__(self, max_size, is_increasing = False):
    self.max_size = max_size
    self.is_increasing = is_increasing
    self.stack = []
  
  def stack_condition(self, value):
    if not self.stack:
      return False
    if self.is_increasing:
      return self.stack[-1] < value 
    else:
      return self.stack[-1] > value

  def push(self, value):
    #  here we check for overflow, regardless of the value
    if len(self.stack) == self.max_size:
      raise Exception("Stack is full.")
    while self.stack and self.stack_condition(value):
      self.stack.pop()
    self.stack.append(value)
  
  def pop(self):
    if len(self.stack) == 0:
      raise Exception("Stack is empty.")
    value = self.stack.pop()
    return value
  
  def is_empty(self):
    return len(self.stack) == 0
  
  def peek(self):
    if len(self.stack) == 0:
      raise Exception("Stack is empty.")
    value = self.stack[-1]
    return value
  

s = MonotonicStack(4, True)
s.push(6)
s.push(4)
s.push(3)
s.push(2)
s.push(7) # should this throw an exception or should this allow to be pushed?

# RECAP
#  1. if using an array, use len() for capturing size, otherwise you need to carefully track the size of the array.
#  2. you need to decide a few more things up front:
#     what happens when the increasing or decreasing property is violated? do you pop() or raise an exception? if you pop(), then do you wait to evaluate if the new value can be added before raising an overflow scenario, or do evaluate if overflow exists first?
    


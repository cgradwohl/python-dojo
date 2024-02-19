class MonotonicIncreasingStack:
  def __init__(self):
      self.stack = []

  def push(self, item):
    while self.stack and self.stack[-1] < item:
        self.stack.pop()
    self.stack.append(item)

stack = MonotonicIncreasingStack()
stack.add(5)
stack.add(4)
stack.add(3)
stack.add(2)
stack.add(1)

print(stack.stack)

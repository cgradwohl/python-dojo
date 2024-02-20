class PriorityQueue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item, priority):
    self.queue.append((item, priority))

  def dequeue(self):
    if not self.queue:
      raise Exception("The queue is empty.")
    prioritized = sorted(self.queue, key=lambda x: x[1])
    item = prioritized.pop(0)
    self.queue = prioritized
    return item[0]
  
q = PriorityQueue()

q.enqueue("creature", 2)
q.enqueue("...", 3)
q.enqueue("hello", 1)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# print(q.dequeue()) # should raise exception

# Follow up:
# what are the pros and cons of doing the sort on the pop() instead of the push()

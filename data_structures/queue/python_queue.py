from queue import Queue
from collections import deque

class MyQueue:
  def __init__(self):
    self.q = Queue()
  
  def enqueue(self, value):
    self.q.put(value)
  
  def dequeue(self):
    return self.q.get()
  


q = MyQueue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

# res1 = q.dequeue()
# print(res1)
# res2 = q.dequeue()
# print(res2)
# res3 = q.dequeue()
# print(res3)
# res4 = q.dequeue()
# print(res4)
# res5 = q.dequeue()
# print(res5)

n = 5
for i in range(1, n+1):
  print(i)


s = "no x in nixon"
print("".join(s.split(" ")))

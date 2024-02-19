rear = 9
front = 0
size = 10

def isFull1():
  return (rear == (front - 1) % (size - 1))

# if the back pointer is directly behind the front pointer, then we are full
def isFull2():
  return (rear + 1) % size == front


print(isFull1())
print(isFull2())

class CircularQueue:
    def __init__(self, capacity):
        self.front = self.rear = -1
        self.size = capacity
        self.queue = [None] * capacity

    def isFull(self):
        # Check if the queue is full
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        # Check if the queue is empty
        return self.front == -1

    def enqueue(self, element):
        if self.isFull():
            print("Queue is Full")
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        return True

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1  # Resetting the queue because it's now empty
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()

# Example of using the CircularQueue
capacity = 5
cq = CircularQueue(capacity)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
# Trying to add another element should fail because the queue is full
cq.enqueue(6)  # This should print "Queue is Full"

cq.display()  # Displays the queue

import sys

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def isEmpty(self):
        return self.storage == []

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    if len(self.storage) >= 1:
      sec_store = self.storage[:1].pop()
      self.storage.pop(0)
      return sec_store

  def len(self):    
    return len(self.storage)
    
  def printQueue(self):
        for items in self.storage:
              print(items)


q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printQueue()
        

class Queue:
    max_size = 10

    def __init__(self):
        self.items = []
        self.rear = 0
        self.front = -1

    def is_empty(self):
        return (self.front > self.rear)
    
    def is_full(self):
        return (self.rear+1 == self.max_size)
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
       
        self.rear += 1
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None 

        return item
    

q = Queue()
q.enqueue(1)
q.dequeue()
print(q.items)
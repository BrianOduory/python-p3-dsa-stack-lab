class Stack:
    
    def __init__(self, items=None, limit=None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit
    
    def push(self, value):
        if self.limit is not None and len(self.items) >= self.limit:
            return
        self.items.append(value)
    
    def pop(self):
        if self.empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return len(self.items) == 0
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit
    
    def search(self, value):
        try:
            index = len(self.items) - 1 - self.items[::-1].index(value)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
    
    def __str__(self):
        return f"Stack({self.items})"
    
    def __repr__(self):
        if self.limit is None:
            return f"Stack()"
        else:
            return f"Stack(limit={self.limit})"
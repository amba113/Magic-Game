from collections.abc import Sequence

class Stack():
    def __init__(self, data = None):
        if data:
            self.data = [data]
        else:
            self.data = []
    
    def empty(self):
        if len(self.data) == 0:
            return True
        return False
        
    def size(self):
        return len(self.data)
    
    def top(self):
        if not self.empty():
            return self.data[-1]
        return None
    
    def peek(self):
        return self.top()
        
    def push(self, item):
        self.data += [item]
        return self.data
    
    def pop(self):
        if not self.empty():
            val = self.data[-1]
            self.data.remove(val)
            return val
        return False
         
    def __str__(self):
        return str(self.data)
        
        
    def __getitem__(self, i):
        return self.data[i]
        
    def __len__(self):
        return len(self.data)

if __name__ == "__main__":
    a = Stack([1])
    print(a.empty())
    print(a.size())
    print(a.top())
    print(a.push(1))
    print(a.push(2))
    print(a.push(3))
    print(a.pop())
    print(a)
    print(len(a))
    print(a[0])


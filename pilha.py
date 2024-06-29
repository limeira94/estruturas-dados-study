class Stack:
    def __init__(self):
        self.values = [0] * 10
        self.top = -1
        
    def push(self, val):
        self.top += 1
        self.values[self.top] =val
        
    def is_empty(self):
        return self.top == -1
    
    def if_full(self):
        return self.top == 9 
    
    def pop(self):
        elem = self.values[self.top]
        self.top -= 1
        return elem


def converter(number):
    p = Stack()
    rest = 0

    while number != 0:
        rest = number % 2
        p.push(rest)
        number = number // 2

    while not p.is_empty():
        rest = p.pop()
        print(rest, end="")
        
    print("\nEnd of program")
    

if __name__ == '__main__':
    converter(172)
    
from matplotlib.pyplot import cla


class Stack:

# Constructor
    def __init__(self) :
        self.top = -1
        self.max_item = 50
        self.list = ["Empty"] * 50

# Transformer
    def Push(self, item) :
        if self.top == 49 :
            print("Stack is Full")
        else :
            self.top += 1
            self.list[self.top] = item
    
    def Pop(self) :
        if self.is_empty() :
            print("Stack is Empty")
        else :
            result = self.list[self.top]
            self.top -= 1
            return result


# Observer
    def is_full(self) :
        if self.top == 49 :
            return True
        else :
            return False
    
    def is_empty(self) :
        if self.top == -1 :
            return True
        else :
            return False
    
    def Top(self) :
        return self.list[self.top]


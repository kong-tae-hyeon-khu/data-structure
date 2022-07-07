class Sorted :
    def __init__(self) :
        self.list = ["Empty" * 100]
        self.length = 0
        self.currentPos = -1
        self.max_items = 100  
    
# Transformers
    # Insert  : How to use Binary Search.
    # Time Complexity : O(n) 
    def Insert_item(self, item):
        if self.length == self.max_items :
            print("List is Full")
        else :
            location = 0
            more_to_search = (location < self.length)

            while more_to_search :
                
                if self.list[location] == "Empty" or self.list[location] < item :
                    break
                elif self.list[location] > item :
                    location += 1
                    more_to_search = (location < self.length)
            for index in range(self.length , location, -1) :
                self.list[index] = self.list[index - 1]
            
            self.list[location] = item
            self.length += 1
# Observers


# Iterators
    def print_elements(self) :
        for i in range(0, self.length) :
            if self.list[i] == "Empty" :
                break
            else :
                print(self.list[i])
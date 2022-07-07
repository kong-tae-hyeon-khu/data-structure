class Sorted :
    def __init__(self) :
        self.list = ["Empty"] * 100
        self.length = 0
        self.current_pos = -1
        self.max_items = 100  
    
# Transformers
    # Insert  : How to use Binary Search ... ?
    # Time Complexity : O(n) 
    def Insert_item(self, item):
        if self.length == self.max_items :
            print("List is Full")
        else :
            location = 0
            more_to_search = (location < self.length)

            while more_to_search :
                if self.list[location] == "Empty" or self.list[location] > item :
                    break
                elif self.list[location] < item :
                    location += 1
                    more_to_search = (location < self.length)

            for index in range(self.length , location, -1) :
                self.list[index] = self.list[index - 1]
            
            self.list[location] = item
            self.length += 1

    # Delete : Using a Binary Search
    def Delete_item(self, item) : 

        result = self.Retrieve_item(item)

        if result == -1 :
            print("item doesn't exist in that list")
            return
        else :
            for index in range(result , self.length) :
                if index == "Empty" :
                    break
                else :
                    self.list[index] = self.list[index + 1] # Cover item.
        self.length -= 1
       
    def Get_next_item(self) :
        result = self.list[self.current_pos]
        self.current_pos += 1
        return result

# Observers
    # Using a Binary Serach
    # Time Complexity : O(log N)
    
    def Retrieve_item(self, item) : 
        first = 0
        last = self.length - 1

        while first <= last :

            mid = int((first + last) / 2 )
            
            if self.list[mid] > item :
                last = mid - 1

            elif self.list[mid] < item :
                first = mid + 1

            elif self.list[mid] == item :
                return mid
        return -1
                 

    def Length_is(self) :
        return self.length
    
    def Is_full(self) :
        return self.length == self.max_items


# Iterators
    def print_elements(self) :
        for i in range(0, self.length) :
            if self.list[i] == "Empty" :
                break

            else :
                print(self.list[i], end= ' ')
        print(' ')
    
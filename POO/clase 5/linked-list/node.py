class Node:
    def __init__(self, value, next = None):
        self.value = value 
        self.next = next 

    @property
    def value(self):
        return self.__value
    

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value
        
    
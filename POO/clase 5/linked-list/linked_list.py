from node import Node

class LinkedList:
    def __init__ (self):
        self.__head = None

    @property
    def head(self):
        return self.__head
    

    def add(self, value):

        if self.__head == None:
            self.__head = Node(value, None)
        else:
            current_node = self.__head
            while True:

                if current_node.next == None:
                    current_node.next = Node(value, None)
                    break

                current_node = current_node.next



    def print_elements(self):
        if self.__head == None:
            print()
            return
        
        current_node = self.__head
        while True:
            print(current_node.value, end = '-->')
            if current_node.next == None:
                break
            current_node = current_node.next


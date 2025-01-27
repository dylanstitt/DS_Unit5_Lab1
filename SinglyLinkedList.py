class SinglyLinkedList:

    class SinglyNode:
        """Nested Singly Node Class"""

        def __init__(self, val):
            """Singly Node Constructor"""
            self.value = val
            self.next = None

        def __str__(self):
            """Singly Node String Method"""
            return f"|{self.value}|"

        def set_next(self, node):
            """Sets the self.next to a new node"""
            if type(node) == type(self) or node is None:
                self.next = node
            else:
                raise TypeError

    def __init__(self):
        """Singly Linked List Constructor"""
        self.head = None
        self.tail = None
        self.__size = 0

    def __str__(self):
        """Singly Linked List String Method"""
        out = "HEAD > "

        walk = self.head
        for i in range(self.__size):
            out += f"{walk} "
            walk = walk.next
            if walk != None:
                out += "-> "

        out += "< TAIL"
        return out

    def __len__(self):
        """Returns the length of the singly linked list"""
        return self.__size

    def __is_empty(self):
        """Returns if the linked list is empty"""
        return self.__size == 0

    def head_insert(self, val):
        """Insert a node at the head of the singly linked list"""
        node = self.SinglyNode(val)
        node.set_next(self.head)

        if self.__is_empty():
            self.head = node
            self.tail = node
        else:
            self.head = node

        self.__size += 1

    def tail_insert(self, val):
        """Insert a node at the tail of the singly linked list"""
        node = self.SinglyNode(val)

        if type(self.tail) == self.SinglyNode:
            self.tail.set_next(node)

        if self.__is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail = node

        self.__size += 1

    def head_remove(self):
        """Remove and return the head of the singly linked list"""
        if self.__is_empty():
            raise ValueError("Singly Linked List is empty")
        else:
            h = self.head
            self.head = self.head.next
            self.__size -= 1

            if self.__is_empty():
                self.head = None
                self.tail = None
            return h.value

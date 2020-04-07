class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        #### My version
        # current_position = 0
        # if self.head:
        #     current = self.head
        #     current_position = 1
        #     if position > current_position:
        #         while current.next:
        #             current = current.next
        #             current_position += 1
        #             if position == current_position:
        #                 break
        # if current_position == position:
        #     return current
        # else:
        #     return None
        #### Udacity version
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        #### My version
        # if self.head:
        #     if position == 1:
        #         new_element.next = self.head
        #         self.head = new_element
        #         return
        #     current = self.head
        #     current_position = 1
        #     while current.next:  # this may lead to logical error
        #         if current_position == position - 1:
        #             new_element.next = current.next
        #             current.next = new_element
        #             return
        #         current = current.next
        #         current_position += 1
        # else:
        #     self.head = new_element
        #### Udacity version
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        #### Udacity version
        # current = self.head
        # previous = None
        # while current.value != value and current.next:
        #     previous = current
        #     current = current.next
        # if current.value == value:
        #     if previous:
        #         previous.next = current.next
        #     else:
        #         self.head = current.next
        #### My version
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
                return
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        if self.head:
            ret = self.head
            self.head = ret.next
            ret.next = None
            return ret
        else:
            return None


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print(ll.head.next.next.value)
    # Should also print 3
    print(ll.get_position(3).value)

    # Test insert
    ll.insert(e4, 3)
    # Should print 4 now
    print(ll.get_position(3).value)

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print(ll.get_position(1).value)
    # Should print 4 now
    print(ll.get_position(2).value)
    # Should print 3 now
    print(ll.get_position(3).value)

    ll2 = LinkedList()
    ll2.delete(1)

try:
    from .linkedlist import LinkedList, Element
except ModuleNotFoundError as e:
    from linkedlist import LinkedList, Element


class StackLL(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """Push (add) a new element onto the top of the stack"""
        self.ll.insert_first(new_element)

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        return self.ll.delete_first()


class StackList:
    def __init__(self, top=None):
        if top is not None:
            self.array = [top]
        else:
            self.array = []

    def push(self, new_element):
        """Push (add) a new element onto the top of the stack"""
        self.array.append(new_element)

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        try:
            return self.array.pop()
        except IndexError as e:
            return None


Stack = StackList
if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)

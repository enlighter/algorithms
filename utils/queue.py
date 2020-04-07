"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""
# from timeit import default_timer as timer


class Queue:
    def __init__(self, head=None):
        if head is not None:
            self.storage = [head]
        else:
            self.storage = []

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        try:
            return self.storage[0]
        except IndexError as e:
            return None

    def dequeue(self):
        try:
            return self.storage.pop(0)
        except IndexError as e:
            return None


if __name__ == '__main__':
    # start = timer()
    # for _ in range(10000):
        # Setup
        q = Queue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test peek
        # Should be 1
        print(q.peek())

        # Test dequeue
        # Should be 1
        print(q.dequeue())

        # Test enqueue
        q.enqueue(4)
        # Should be 2
        print(q.dequeue())
        # Should be 3
        print(q.dequeue())
        # Should be 4
        print(q.dequeue())
        q.enqueue(5)
        # Should be 5
        print(q.peek())
    # end = timer()
    # print('Average time taken: {}s'.format((end-start)/10000))

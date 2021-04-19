# Name: Clara  Watson
# OSU Email: watsoncl@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Linked-List-and-ADT-Implementation
# Due Date: Monday April 15, 2021

from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def _increment(self, index: int) -> int:
        """
        Move index to next position
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self._current_size >= self._sa.length():
            self._double_queue()
        else: 
            self._current_size = self._current_size

        self._back = self._increment(self._back)
        self._current_size += 1
        self._sa.set(self._back, value)

    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise QueueException
        else:
            value = self._sa.get(self._front)
            self._sa.set(self._front, None)
            self._front = self._increment(self._front)
            self._current_size -= 1
        return value

    def front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise QueueException
        return self._sa.get(self._front)

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        size = self._current_size
        new = self._sa.length()*2
        end = self._sa.length()
        count = 0
        double = False
        if  size >= self._sa.length():
            arr = StaticArray(new)
            double = True 
        else: 
            double = False 
        for i in range(self._front, end):
            arr[count] = self._sa.get(i)
            count += 1
        if self._front == 0:
            if double:
                count = count 
        else:
            for i in range(self._front):
                arr[count] = self._sa.get(i)
                count += 1
        
        self._front = 0
        self._back = count-1
        self._sa = arr

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)

    print('\n# front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)

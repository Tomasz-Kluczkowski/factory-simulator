from typing import List, Any


class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """
        Inserts item at the beginning of the queue.

        Parameters
        ----------
        item
            Item to insert.
        """
        self._items.insert(0, item)

    def dequeue(self):
        """
        Returns last item in the queue.
        """
        return self._items.pop()

    @property
    def is_empty(self) -> bool:
        """
        Returns true if queue is empty, false otherwise.
        """
        return len(self._items) == 0

    @property
    def size(self) -> int:
        """
        Returns number of items in the queue.
        """
        return len(self._items)

    @property
    def items(self) -> List[Any]:
        """
        Returns contents of the queue as a list.
        """
        return self._items


class MaxSizeQueue(Queue):
    pass

from simulation.helpers.data_structures import Queue


class TestQueue:
    def test_init(self):
        queue = Queue()
        assert queue.size == 0
        assert queue.items == []

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.items == [2, 1]

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.size == 2

    def test_is_empty_returns_true(self):
        queue = Queue()
        assert queue.is_empty

        queue.enqueue(1)
        queue.dequeue()
        assert queue.is_empty

    def test_is_empty_returns_false(self):
        queue = Queue()
        queue.enqueue(1)
        assert not queue.is_empty

        queue.dequeue()
        assert queue.is_empty

    def test_size(self):
        queue = Queue()
        assert queue.size == 0

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.size == 3

"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""


def has_duplicates(product_ids):
    seen_ids = set()

    for product_id in product_ids:
        if product_id in seen_ids:
            return True

        seen_ids.add(product_id)

    return False


# A set fits this problem because it stores unique values and supports fast
# membership checks. Each lookup and insertion is O(1) on average, making the
# full function O(n) instead of comparing every pair in O(n²) time.


"""
Problem 2: Order Manager

Maintain tasks in the order they were added and support removing tasks
from the front.
"""

from collections import deque


class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None

        return self.tasks.popleft()


# A queue is appropriate because tasks must be removed in the same order they
# were added. A deque provides O(1) insertion at the rear and O(1) removal from
# the front, while removing index 0 from a regular list would take O(n) time.


"""
Problem 3: Unique Value Counter

Receive a stream of integers and return the number of unique values seen.
"""


class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)


# A set is the best fit because it automatically ignores duplicate values.
# Adding a value takes O(1) average time, and getting the stored set's length
# takes O(1) time.


if __name__ == "__main__":
    assert has_duplicates([10, 20, 30, 20, 40]) is True
    assert has_duplicates([1, 2, 3, 4, 5]) is False
    assert has_duplicates([]) is False

    task_queue = TaskQueue()
    assert task_queue.remove_oldest_task() is None

    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")

    assert task_queue.remove_oldest_task() == "Email follow-up"
    assert task_queue.remove_oldest_task() == "Code review"

    tracker = UniqueTracker()
    assert tracker.get_unique_count() == 0

    tracker.add(10)
    tracker.add(20)
    tracker.add(10)

    assert tracker.get_unique_count() == 2

    print("All practice problem tests passed.")

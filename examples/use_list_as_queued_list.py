from collections import deque

# Deques are a generalization of stacks and queues
#  (the name is pronounced “deck” and is short for “double-ended queue”).
# Deques support thread-safe, memory efficient
#  appends and pops from either side of the deque
#  with approximately the same O(1) performance
#  in either direction.

x = 3
queue = deque([i for i in range(1, 10)])  # Deque returns a new deque object initialized left-to-right
queue.append(x)  # Add x to the right side of the deque.
queue.appendleft(x)  # Add x to the left side of the deque.

queue.popleft()  # Remove and return an element from the left side of the deque.
queue.pop()  # Remove and return an element from the right side of the deque.
# If no elements are present, raises an IndexError.

queue.remove(x)  # Remove the first occurrence of value.
# If not found, raises a ValueError.

queue.count(x)  # Count the number of deque elements equal to x.

queue.clear()  # Remove all elements from the deque leaving it with length 0.

iterable = [i for i in range(10)]
queue.extend(iterable)  # Extend the right side of the deque by appending elements from the iterable argument.
queue.extendleft(iterable)  # Extend the left side of the deque by appending elements from iterable.
# Note, the series of left appends results in reversing the order of elements in the iterable argument.
# out: deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

queue.index(x)  # Return the position of x in the deque (at or after index start and before index stop)
# Returns the first match or raises ValueError if not found.

queue.remove(x)  # Remove the first occurrence of x. If not found, raises a ValueError.

i = 3
queue.insert(i, x)  # Insert x into the deque at position i.
# If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.
# out: deque([9, 8, 7, 3, 6, 5, 4, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

queue.reverse()  # Reverse the elements of the deque in-place and then return None.
# out: deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 4, 5, 6, 3, 7, 8, 9])


n = 4
queue.rotate(n)  # Rotate the deque n steps to the right. If n is negative, rotate to the left.
# Rotating one step to the right is equivalent to: d.appendleft(d.pop()).

queue.maxlen  # Maximum size of a deque or None if unbounded.

queue.clear()
print(queue)  # out: deque([])

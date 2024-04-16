from collections import deque

def reverse_queue(queue):
    reversed_queue = deque()
    while queue:
        reversed_queue.append(queue.pop())
    return reversed_queue

class FreqStack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        max_freq = max([self.stack.count(i) for i in set(self.stack)])
        max_freq_elements = [key for key in set(self.stack) if self.stack.count(key) == max_freq]
        reversed_stack = reverse_queue(self.stack)
        for i in reversed_stack:
            if i in max_freq_elements:
                el = i
                reversed_stack.remove(i)
                self.stack = reverse_queue(reversed_stack)
                break
        return el


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def popleft(self):
        if self.head:
            res = self.head.value
            self.head = self.head.next
            return res
    
    def top(self):
        if self.head:
            return self.head.value

    def empty(self):
        return self.head is None

    def append(self, x: int):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(x)
        else:
            self.head = Node(x)
    
class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while not self.queue1.empty():
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        if not self.queue1.empty():
            elem = self.queue1.popleft()
            self.push(elem)
            return elem
        elif not self.queue2.empty():
            elem = self.queue2.popleft()
            self.push(elem)
            return elem

    def empty(self) -> bool:
        return self.queue1.empty() and self.queue2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
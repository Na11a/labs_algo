class Element:
    def __init__(self, value, priority: int):
        self.value = value
        self.priority = priority

    def __str__(self):
        return f'Value : {self.value}, Priority : {self.priority}'


class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, value, priority):
        self._heap.append(Element(value, priority))
        self._bottom_up(len(self) - 1)

    def peek(self):
        if self.__len__() == 0:
            return None
        return self._heap[0].value

    def pop(self):
        if self._heap:
            self._heap[len(self) - 1], self._heap[0] = self._heap[0], self._heap[len(self) - 1]
            root = self._heap.pop()
            self._top_down(0)
            return root.value
        return None

    def __len__(self):
        return len(self._heap)

    def _bottom_up(self, index):
        root_index = (index - 1) // 2
        if root_index < 0:
            return

        if self._heap[index].priority > self._heap[root_index].priority:
            self._heap[index], self._heap[root_index] = self._heap[root_index], self._heap[index]
            self._bottom_up(root_index)

    def _top_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if right_child_index >= len(self._heap):
            return

        if self._heap[largest].priority < self._heap[left_child_index].priority:
            largest = left_child_index
        if self._heap[largest].priority < self._heap[right_child_index].priority:
            largest = right_child_index

        if largest is not index:
            self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
            self._top_down(largest)

    def __str__(self):
        return str([str(el) for el in self._heap])

if __name__=="__main__":
    queue = PriorityQueue()
    queue.push(8,3)
    queue.push(7,1)
    queue.push(2,2)
    queue.push(4,4)
    queue.push(2,1)
    print(queue)
    queue.pop()
    print(queue)

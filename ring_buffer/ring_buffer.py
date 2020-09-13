class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring_buffer = [None] * capacity
        self.cursor = 0

    def append(self, item):
        # if len(self.ring_buffer) < self.capacity:
        #     self.ring_buffer.append(item)
        # if len(self.ring_buffer) >= self.capacity:
        #     self.ring_buffer.pop(0)
        #     self.ring_buffer.insert(0, item)

        self.ring_buffer[self.cursor] = item
        self.cursor += 1
        if self.cursor == self.capacity:
            self.cursor = 0

    def get(self):

        none_check = []

        for item in self.ring_buffer:
            if item is not None:
                none_check.append(item)

        return none_check

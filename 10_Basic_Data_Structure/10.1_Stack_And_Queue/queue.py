class queue:
    def __init__(self,length):
        self.content = [None]*length
        self.length = length
        self.head = 0
        self.tail = 0

    def enqueue(self,value):
        self.content[self.tail]=value
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        value = self.content[self.head]
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
        return value


class stack:
    def __init__(self):
        self.content = []
        self.top = -1

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def push(self,value):
        self.content.append(value)
        self.top += 1

    def pop(self):
        if self.isempty():
            print("Stack underflow")
        else:
            self.top -= 1
            return self.content.pop()

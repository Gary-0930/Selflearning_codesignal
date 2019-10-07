Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        

    def push(self, x: int) -> None:
        self.minStack.append(x)
        return self.minStack

    def pop(self) -> None:
        place = len(self.minStack)
        self.minStack.pop(place - 1)

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        letter = min(self.minStack)
        return letter


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

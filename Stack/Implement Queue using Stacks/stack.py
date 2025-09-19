# Problem Link : https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

        

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())   # return 1
    print(obj.pop())    # return 1
    print(obj.empty())  # return False    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
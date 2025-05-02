#Problem Link : https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == "__main__":
    sol = MinStack()
    sol.push(5)    
    sol.push(2)  
    sol.push(-4)     
    sol.push(-6)

    print("Top:", sol.top())      
    print("Min:", sol.getMin()) 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
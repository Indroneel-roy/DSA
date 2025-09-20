# Problem Link : https://leetcode.com/problems/online-stock-span/
from typing import List
class StockSpanner:
    #Brute Force solution
    # def __init__(self):
    #     self.arr = []
        

    # def next(self, price: int) -> int:
    #     self.arr.append(price)
    #     i = len(self.arr) - 2
    #     while i >= 0 and self.arr[i] <= price:
    #         i -= 1
    #     return len(self.arr) - i - 1    
    
    #Monotonic decreasing stack
    def __init__(self):
        self.stack = [] # stack -> (price, span)
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span    
if __name__ == "__main__":
    obj = StockSpanner()
    print(obj.next(100)) # return 1
    print(obj.next(80))  # return 1
    print(obj.next(60))  # return 1
    print(obj.next(70))  # return 2
    print(obj.next(60))  # return 1
    print(obj.next(75))  # return 4
    print(obj.next(85))  # return 6    

        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
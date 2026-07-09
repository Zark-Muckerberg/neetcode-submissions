class StockSpanner:

    def __init__(self):
        self.stack=[]
        
    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            #if price of previous was lower than current, we know that the previous span is lower than current
            #add span of previous to span of current
            span = self.stack[-1][1]+span
            #remove the element after we add its span
            self.stack.pop()

            #after popping, still have to loop back to check 
        self.stack.append((price,span))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
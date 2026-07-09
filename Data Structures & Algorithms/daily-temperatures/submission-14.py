class Solution:
    def dailyTemperatures(self,temperatures: List[int]) -> List[int]:
        
        stack = []
        hotter = 0
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            #while stack not empty and top element less than current element in arr
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop()
                result[x] = i-x
            stack.append(i)    
        return result

        
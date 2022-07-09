'''
Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
'''

#CODE:
  class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range (len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()    

    def top(self) -> int:
        return self.q[-1]
        
    def empty(self) -> bool:
        return len(self.q) == 0
        
        
        

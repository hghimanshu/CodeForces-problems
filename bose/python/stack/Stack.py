import collections
class Stack:
    """
    Implementing stack with Max API
    We will use caching to dramatically improve the time complexity of popping using caching
    """
    ElementWithCachedMax = collections.namedtuple("ElementWithCachedMax",("element","max"))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) ==0

    def max(self):
        if self.empty():
            raise IndexError('max() : empty stack')
        return self._element_with_cached_max[-1].max
    
    def peek(self):
        if self.empty():
            raise IndexError('peek() : empty stack')
        return self._element_with_cached_max[-1]

    def pop(self):
        if self.empty():
            raise IndexError('pop() : empty stack')
        return self._element_with_cached_max.pop().element

    def push(self,x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x,x if self.empty() else max(x,self.max()))
        )


if __name__ == "__main__":
    st = Stack()
    st.push(3)
    print(st.max())
    print(st.peek())
    st.push(1)
    print(st.max())
    print(st.peek())
    st.push(5)
    print(st.max())
    print(st.peek())
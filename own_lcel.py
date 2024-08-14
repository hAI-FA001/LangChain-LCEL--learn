from abc import ABC, abstractmethod


class MyRunnable(ABC):
    def __init__(self):
        # what processing to perform after this one
        self.next = None
    
    @abstractmethod
    def process(self, data):
        pass

    # starts all the processing recursively
    def invoke(self, data):
        out = self.process(data)
        if self.next is not None:
            return self.next.invoke(out)
        return out
    
    # overload the | (pipe) operator
    # left | right
    def __or__(self, right):
        return MyRunnableSequence(self, right)
    
class MyRunnableSequence(MyRunnable):
    def __init__(self, left, right):
        super().__init__()

        self.left = left
        self.right = right
    
    def process(self, data):
        # MyRunnableSequence will only start processing using .invoke() 
        return data
    
    def invoke(self, data):
        # left | right -> right(left(data))
        return self.right.invoke(self.left.invoke(data))


# implement the MyRunnable interface
class AddTen(MyRunnable):
    def process(self, data):
        return data + 10

class MultTwo(MyRunnable):
    def process(self, data):
        return 2 * data

class ToStr(MyRunnable):
    def process(self, data):
        return f"Str: {data}"
    

if __name__ == "__main__":
    data = 10

    add = AddTen()
    mult = MultTwo()
    to_str = ToStr()

    my_chain = add | mult | to_str

    print(my_chain.invoke(data))

    # each MyRunnable has .invoke()
    print(f"{data} -> {add.invoke(data)} -> {mult.invoke(add.invoke(data))} -> {to_str.invoke(mult.invoke(add.invoke(data)))}")
    # using pipe
    print(f"{data} -> {add.invoke(data)} -> {(add | mult).invoke(data)} -> {(add | mult | to_str).invoke(data)}")

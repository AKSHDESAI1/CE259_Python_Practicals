# Aim: Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git
class StackByAKSH:
    __dataList = []

    # regular methods for stack is implemented here...
    def push(self, data):
        self.__dataList.append(data)

    def pop(self):
        if len(self.__dataList) > 0:  # is stack is not empty
            return self.__dataList.pop()  # then pop the element
        else:
            # else print error message...
            return "No elements left for popping operation!"

    def get_stackSize(self):
        return len(self.__dataList)

    def printStack(self):
        print(self.__dataList)

    # traversal methods...for stack is implemented here...
    def has_next(self):
        return bool(len(self.__dataList))

    def next(self):
        return self.pop()

    # modified methods...for stack is implemented here...
    def peek(self):
        if len(self.__dataList) > 0:  # if length of the stack is 0
            return self.__dataList[-1]  # then peek the top element
        else:
            return "No Elements are there in stack."  # else print error element

    def printPeek(self):
        print(self.peek())

    def printPop(self):
        print(self.pop())


if __name__ == "__main__":
    print('Name:- AKSH DESAI, ID:- 20CE020 ')
    stack = StackByAKSH()  # making a reference of stack class...(object)
    stack.printStack()
    stack.push(15)
    stack.printStack()
    stack.push("AKSH")
    stack.push("50")
    print(stack.peek())
    stack.printStack()
    while stack.has_next():  # traversing while list is empty.
        print(stack.next())

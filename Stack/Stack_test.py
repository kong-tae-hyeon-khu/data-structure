from Stack import *

test_stack = Stack()


# Push
test_stack.Push(3)
test_stack.Push(4)
test_stack.Push(1)
test_stack.Push(5)

if (test_stack.is_full()):
    print("Stack is Full")
else :
    print("Stack is not Full")

while (test_stack.is_empty() is not True) :
    print(test_stack.Pop())


if (test_stack.is_empty()):
    print("Stack is Empty")
else :
    print("Stack is not Empty")
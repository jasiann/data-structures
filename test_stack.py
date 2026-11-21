import pytest
from stack import Stack

def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    assert stack.peek() == 2
    assert len(stack) == 2 

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.peek() == 1

def test_len(): 
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2 

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False

def test_pop_from_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
def test_peek_from_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()        
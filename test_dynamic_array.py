import pytest
from dynamicarray import DynamicArray


def test_append_and_resize():
    arr = DynamicArray()

    for x in [10, 20, 30, 40, 50]:
        arr.append(x)

    assert len(arr) == 5
    assert arr.capacity == 8

    for i, x in enumerate([10, 20, 30, 40, 50]):
        assert arr[i] == x


def test_setitem():
    arr = DynamicArray()

    for x in [10, 20, 30, 40, 50]:
        arr.append(x)

    arr[1] = 99

    assert len(arr) == 5

    for i, x in enumerate([10, 99, 30, 40, 50]):
        assert arr[i] == x


def test_pop():
    arr = DynamicArray()

    arr.append(1)
    arr.append(2)
    arr.append(3)

    assert arr.pop() == 3
    assert arr.pop() == 2
    assert arr.pop() == 1

    assert len(arr) == 0


def test_errors():
    arr = DynamicArray()

    with pytest.raises(IndexError):
        arr[5]

    with pytest.raises(IndexError):
        arr[5] = 99

    with pytest.raises(IndexError):
        arr.pop()   

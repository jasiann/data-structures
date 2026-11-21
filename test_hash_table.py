import pytest
from hashtable import HashMap

def test_put_then_get():
    t = HashMap()
    t.put("a", 1)
    assert t.get("a") == 1


def test_missing_key_raises():
    t = HashMap()
    with pytest.raises(KeyError):
        t.get("z")


def test_update_existing_key():
    t = HashMap()
    t.put("a", 1)
    t.put("a", 2)
    assert t.get("a") == 2
    assert len(t) == 1


def test_delete():
    t = HashMap()
    t.put("a", 1)
    t.delete("a")
    with pytest.raises(KeyError):
        t.get("a")
    assert len(t) == 0


def test_collision():
    t = HashMap(capacity=1)
    t.put("a", 1)
    t.put("b", 2)
    t.put("c", 3)
    assert t.get("a") == 1
    assert t.get("b") == 2
    assert t.get("c") == 3
    assert len(t) == 3
    


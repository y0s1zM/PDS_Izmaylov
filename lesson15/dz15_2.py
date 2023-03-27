from binary_tree import BinaryTree

def test_add_element():
    tree = BinaryTree()
    tree.add_element(10)
    assert tree.search(10) == True

def test_find_minimum():
    tree = BinaryTree()
    tree.add_element(10)
    tree.add_element(5)
    tree.add_element(15)
    tree.add_element(3)
    assert tree.find_minimum() == 3

def test_find_maximum():
    tree = BinaryTree()
    tree.add_element(10)
    tree.add_element(5)
    tree.add_element(15)
    tree.add_element(20)
    assert tree.find_maximum() == 20

def test_remove_element():
    tree = BinaryTree()
    tree.add_element(10)
    tree.add_element(5)
    tree.add_element(15)
    tree.add_element(20)
    tree.remove_element(15)
    assert tree.search(15) == False
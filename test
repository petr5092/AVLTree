from AVL_tree import *


def test_1():
    lst = AVLtree()
    for i in [10, 5, 13, 12, 11, 2]:
        lst.insert(i)
    return lst.print_in_order()


def test_2():
    lst = AVLtree()
    for i in [10, 7, 5]:
        lst.insert(i)
    return lst.print_in_order(), lst.root.value


def test_3():
    lst = AVLtree()
    for i in [10, 5, 15, 13, 11, 14, 20]:
        lst.insert(i)
    lst.delete(10)
    return lst.print_in_order(), lst.root.value


def test_control():
    print(test_2())
    print(test_3())


test_control()

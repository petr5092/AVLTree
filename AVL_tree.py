class Node:
    def __init__(self, value, par_node=None):
        self.value = value
        self.parent: Node = par_node
        self.left_child: Node = None
        self.right_child: Node = None
        self.height = 1

    def hasRightChild(self):
        if self.right_child:
            return True
        return False

    def hasLeftChild(self):
        if self.left_child:
            return True
        return False

    def hasBothChild(self):
        if self.right_child and self.left_child:
            return True
        return False

    def isRoot(self):
        if not self.parent:
            return True
        return False

    def isLeftChild(self):
        if self.parent.left_child == self:
            return True
        return False

    def isRightChild(self):
        if self.parent.right_child == self:
            return True
        return False

    def setRightChild(self, node):
        self.right_child = node
        if node is not None:
            node.parent = self

    def setLeftChild(self, node):
        self.left_child = node
        if node is not None:
            node.parent = self


class AVLtree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value, None)

    def _insert(self, cur_node, value, parent):
        if not cur_node:
            cur_node = Node(value, par_node=parent)
        elif cur_node.value > value:
            cur_node.left_child = self._insert(
                cur_node.left_child, value, cur_node)
        elif cur_node.value < value:
            cur_node.right_child = self._insert(
                cur_node.right_child, value, cur_node)
        cur_node = self.balance(cur_node)
        return cur_node

    def balance(self, cur_node):
        cur_node.height = self.fix_height(cur_node)
        cur_node = self._balance(cur_node)
        return cur_node

    def _balance(self, cur_node):
        if self.balance_factor(cur_node) == 2:
            if self.balance_factor(cur_node.right_child) == -1:
                cur_node.right_child = self._turn_right(cur_node.right_child)
            cur_node = self._turn_left(cur_node)
        elif self.balance_factor(cur_node) == -2:
            if self.balance_factor(cur_node.left_child) == 1:
                cur_node.left_child = self._turn_right(cur_node.left_child)
            cur_node = self._turn_right(cur_node)
        return cur_node

    def get_height(self, cur_node):
        if cur_node:
            return cur_node.height
        return 0

    def fix_height(self, cur_node):
        return max(self.get_height(cur_node.right_child), self.get_height(cur_node.left_child)) + 1

    def balance_factor(self, cur_node):
        if cur_node:
            return self.get_height(cur_node.right_child) - self.get_height(cur_node.left_child)
        return 0

    def _turn_left(self, q: Node):
        q_parent = q.parent
        p = q.right_child
        b = p.left_child
        p.setLeftChild(q)
        q.setRightChild(b)
        p.parent = q_parent
        q.height = p.height - 1
        return p

    def _turn_right(self, p: Node):
        p_parent = p.parent
        q = p.left_child
        b = q.right_child
        q.setRightChild(p)
        p.setLeftChild(b)
        q.parent = p_parent
        p.height = q.height - 1
        return q

    def print_in_order(self):
        if self.root:
            answer_list = []
            self._print_in_order(self.root, answer_list)
            return answer_list

    def _print_in_order(self, cur_node, answer_list):
        if cur_node.left_child:
            self._print_in_order(cur_node.left_child, answer_list)
        answer_list.append(
            [cur_node.value, cur_node.parent.value if cur_node.parent is not None else None, cur_node.height])
        if cur_node.right_child:
            self._print_in_order(cur_node.right_child, answer_list)

    def delete(self, value):
        if self.root is not None:
            self.root = self._delete(value, self.root)
            

    def _delete(self, value, cur_node: Node):
        if value == cur_node.value:
            print('We find cur_node', cur_node.value)
            cur_node = self._delete_(cur_node)
        elif value > cur_node.value:
            cur_node.right_child = self._delete(value, cur_node.right_child)
        elif value < cur_node.value:
            cur_node.left_child = self._delete(value, cur_node.left_child)
        cur_node = self.balance(cur_node)
        return cur_node
    
    def _find_maxLeft(self, cur_node: Node):
        if cur_node.right_child:
            cur_node = cur_node.right_child
            cur_node = self._find_maxLeft(cur_node)
        return cur_node
    
    def _delete_(self, cur_node: Node):
        if not cur_node.hasBothChild():
            if cur_node.hasLeftChild():
                cur_node = cur_node.left_child
            elif cur_node.hasRightChild():
                cur_node = cur_node.right_child
            else:
                cur_node = None
            return cur_node
        elif cur_node.hasBothChild():
            max_left = self._find_maxLeft(cur_node.left_child)
            cur_node.right_child.parent = max_left
            max_left.right_child = cur_node.right_child
            if max_left.parent != cur_node:
                max_left.left_child = cur_node.left_child
            max_left.parent.right_child = None
            max_left.parent = cur_node.parent
            return max_left










class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self, compare_func=None):
        self.compare = compare_func if compare_func else lambda x, y: (x > y) - (x < y)

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif self.compare(key, root.key) < 0:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return self.balance(root, key)

    def delete(self, root, key):
        if not root:
            return root
        elif self.compare(key, root.key) < 0:
            root.left = self.delete(root.left, key)
        elif self.compare(key, root.key) > 0:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        if root is None:
            return root

        return self.balance(root, key)

    def balance(self, root, key):
        if root is None:
            return None
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        if z is None:
            return None
        y = z.right
        if y is None:
            return z
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, y):
        if y is None:
            return None
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if root:
            yield root.key
            yield from self.preOrder(root.left)
            yield from self.preOrder(root.right)

    def inOrder(self, root):
        if root:
            yield from self.inOrder(root.left)
            yield root.key
            yield from self.inOrder(root.right)

    def search(self, root, key):
        if root is None or self.compare(root.key, key) == 0:
            return root
        if self.compare(root.key, key) < 0:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def lower(self, root, key):
        if root is None:
            return None

        if self.compare(key, root.key) <= 0:
            return self.lower(root.left, key)
        else:
            right = self.lower(root.right, key)
            return right if right is not None else root.key

    def higher(self, root, key):
        if root is None:
            return None

        if self.compare(key, root.key) >= 0:
            return self.higher(root.right, key)
        else:
            left = self.higher(root.left, key)
            return left if left is not None else root.key


class TreeSet:
    def __init__(self, compare_func=None):
        self.tree = AVLTree(compare_func)
        self.root = None

    def add(self, key):
        if self.root is None or not self.tree.search(self.root, key):
            self.root = self.tree.insert(self.root, key)

    def remove(self, key):
        if self.root is not None and self.tree.search(self.root, key):
            self.root = self.tree.delete(self.root, key)

    def lower(self, key):
        return self.tree.lower(self.root, key)

    def higher(self, key):
        return self.tree.higher(self.root, key)

    def __contains__(self, key):
        return self.tree.search(self.root, key) is not None

    def __iter__(self):
        yield from self.tree.inOrder(self.root)


if __name__ == "__main__":

    def test_tree_set():
        array = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 2], [3, 5]]
        # 如果第一个元素相等则按照第二个元素的逆序排列
        # ts = TreeSet(lambda x, y: x[0] - y[0] if x[0] != y[0] else x[1] - y[1])
        ts = TreeSet()

        # 测试所有功能
        for i in array:
            ts.add(i)
        print(list(ts))

        ts.remove([3, 4])
        print(list(ts))
        ts.remove([3, 4])
        print(list(ts))

        print([ts.lower([3, 4]), ts.higher([30, 4])])

    test_tree_set()

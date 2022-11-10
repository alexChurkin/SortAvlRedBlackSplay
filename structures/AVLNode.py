class AVLNode(object):
    """ Звено AVL-дерева."""

    def __init__(self, parent, k):
        """
        Создаёт звено.

        Принимает:
            parent: Родительское звено.
            k: Ключ звена.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def print(self):
        self._printRec(self)

    def _printRec(self, root, tabCount=0):
        if root is None:
            return

        for i in range(0, tabCount):
            print("  ", end='')

        print(root.key, tabCount)
        self._printRec(root.left, tabCount + 1)
        self._printRec(root.right, tabCount + 1)

    def find(self, k):
        """
        Находит звено с ключом k в поддереве с корнем self.

        Принимает:
            k: Ключ звена, которое мы хотим отыскать.

        Возвращает:
            Звено с ключом k.
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def findMin(self):
        """
        Находит звено с минимальным ключом в поддереве с корнем self.

        Возвращает:
            Звено с минимальным ключом
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def insert(self, node):
        """
        Производит вставку звена в поддерево с корнем self.

        Принимает:
            node: Звено для вставки.
        """

        if node is None:
            # Вставить звено некуда
            return
        if node.key <= self.key:
            # Ключ вставляемого звена меньше текущего ключа
            if self.left is None:
                # Слева пусто - можно присоединить новое звено
                node.parent = self
                self.left = node
            else:
                # Слева не пусто - идём влево вниз и ищем место вставки дальше
                self.left.insert(node)
        else:
            # Ключ вставляемого звена больше текущего ключа
            if self.right is None:
                # Справа пусто - можно присоединить новое звено
                node.parent = self
                self.right = node
            else:
                # Справа не пусто - идём вправо вниз и ищем место вставки дальше
                self.right.insert(node)
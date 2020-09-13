from queue import Queue


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def addNewNode(self, newValue) -> None:
        """
            
        """
        if self.value == None:
            self.value = newValue
        else:
            self._addNewNode(newValue, self)

    def _addNewNode(self, newValue, node):
        if newValue < node.value:
            if node.left == None:
                node.left = BinaryNode(newValue)
            else:
                node._addNewNode(newValue, node.left)
        elif newValue > self.value:
            if node.right == None:
                node.right = BinaryNode(newValue)
            else:
                node._addNewNode(newValue, node.right)

    def printTraverseDepthFirst(self) -> None:
        """
            Traverses through nodes from left to right
                5
            4       7
            Will print:
            5 - 1
            4 - 2
            7 - 3
        """
        children = Queue()
        children.put(self)
        count = 1
        while children.empty() != True:
            node = children.get()
            print(f"{node} - {count}")
            count+=1
            if node.left != None:
                children.put(node.left)
            if node.right != None:
                children.put(node.right)

    def __str__(self):
        return f"{self.value}"


def main():
    root = BinaryNode(10)
    root.addNewNode(4)
    root.addNewNode(15)
    root.addNewNode(6)
    root.addNewNode(34)
    root.addNewNode(1)
    root.printTraverseDepthFirst()


if __name__ == '__main__':
    main()

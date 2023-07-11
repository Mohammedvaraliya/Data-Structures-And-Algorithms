from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_max_dept(self, traversal_type):
        if traversal_type == "maximum_depth":
            return self.maxDepth(self.root)
        elif traversal_type == "maximum_depth_BFS":
            return self.maxDepth_BFS(self.root)
        else:
            print("Depth type " + str(traversal_type) + " is not supported.")
            return False

    def maxDepth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth_BFS(self, root):
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        return level



        

if __name__ == "__main__":

    tree1 = BinaryTree(3)
    tree1.root.left = Node(9)
    tree1.root.right = Node(20)
    tree1.root.right.left = Node(15)
    tree1.root.right.right = Node(7)

    X = tree1.print_max_dept("maximum_depth_BFS")
    print(X)

    tree2 = BinaryTree(1)
    tree2.root.right = Node(2)

    Y = tree2.print_max_dept("maximum_depth")
    print(Y)

    
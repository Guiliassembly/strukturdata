class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   

class postfixTree:
    def __init__(self):
        self.root = None

    def treeOperation(self, postfix):
        stack = []
        for char in postfix:
            if char.isdigit():  # if operand, push node operand ke stack
                stack.append(Node(char))
            else:  # if operator, char menjadi node dengan 2 anak pop dari stack
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        self.root = stack.pop()

    def evaluate(self, node):
        if node is None:
            return 0
        # return angkanya kalo tidak ada anak lain 
        if node.left is None and node.right is None:
            return int(node.value)
        # check untuk subtree kanan kiri
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        # kalo
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

    def infix(self, node): # ganti infix
        if node:
            self.infix(node.left)
            print(node.value, end=" ")
            self.infix(node.right)

    def prefix(self, node): # ganti prefix
        if node:
            print(node.value, end=" ")
            self.prefix(node.left)
            self.prefix(node.right)
# testing
repeat:bool = True
while (repeat):
    #enter expression untuk di evaluate
    expression = input("enter a postfix expression: ") 
    tree = postfixTree()
    tree.treeOperation(expression)

    #print result dari expression
    print("\nResult of Expression: ")
    print(tree.evaluate(tree.root))

    #print infix
    print("infix: ")
    tree.infix(tree.root)
    
    #print prefix
    print("preorder: ")
    tree.prefix(tree.root)

    #pilihan untuk mengulang lagi 
    print("\nmencoba lagi? (y/n)")
    pilihan = input()
    if pilihan == 'y':
        repeat = True
    elif pilihan == 'n':
        repeat = False    
    else:
        repeat = True
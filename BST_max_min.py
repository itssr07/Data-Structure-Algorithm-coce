class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return


        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if self.key==data:
            print("Node is Found!")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the Tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the Tree!")
                

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("Node with minimum key is :",current.key)

    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("Node with maximum key is :",current.key)


    

root=BST(10)
list1=[6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
print("PREORDER")
root.preorder()
print()
root.min_node()
root.max_node()
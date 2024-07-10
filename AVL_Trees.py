# Định nghĩa lớp Node, đại diện cho một nút trong cây AVL
class Node:
    def __init__(self, key):
        self.key = key  # Giá trị của nút
        self.height = 1  # Chiều cao của nút, ban đầu là 1
        self.left = None  # Con trái của nút
        self.right = None  # Con phải của nút


# Định nghĩa lớp AVLTree, đại diện cho cây AVL và các thao tác trên cây
class AVLTree:
    # Hàm chèn một nút mới vào cây AVL
    def insert(self, root, key):
        if not root:
            return Node(key)  # Nếu cây rỗng, tạo nút mới và trả về nó

        if key < root.key:
            root.left = self.insert(root.left, key)  # Chèn vào cây con bên trái nếu key nhỏ hơn
        else:
            root.right = self.insert(root.right, key)  # Chèn vào cây con bên phải nếu key lớn hơn hoặc bằng

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))  # Cập nhật chiều cao của nút

        balance = self.getBalance(root)  # Lấy hệ số cân bằng

        # Xử lý các trường hợp mất cân bằng
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)  # Trường hợp Left Left
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)  # Trường hợp Right Right
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)  # Trường hợp Left Right
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)  # Trường hợp Right Left

        return root  # Trả về nút đã được cân bằng lại

    # Hàm xóa một nút khỏi cây AVL
    def delete(self, root, key):
        if not root:
            return root  # Nếu cây rỗng, trả về cây rỗng

        if key < root.key:
            root.left = self.delete(root.left, key)  # Xóa từ cây con bên trái
        elif key > root.key:
            root.right = self.delete(root.right, key)  # Xóa từ cây con bên phải
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp  # Nút có tối đa một con, trả về cây con bên phải
            elif root.right is None:
                temp = root.left
                root = None
                return temp  # Nút có tối đa một con, trả về cây con bên trái

            temp = self.getMinValueNode(root.right)  # Nút có hai con, tìm nút nhỏ nhất trong cây con bên phải
            root.key = temp.key  # Sao chép giá trị của nút nhỏ nhất vào nút hiện tại
            root.right = self.delete(root.right, temp.key)  # Xóa nút nhỏ nhất trong cây con bên phải

        if root is None:
            return root  # Nếu cây chỉ có một nút, trả về cây rỗng

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))  # Cập nhật chiều cao của nút

        balance = self.getBalance(root)  # Lấy hệ số cân bằng

        # Xử lý các trường hợp mất cân bằng
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)  # Trường hợp Left Left
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)  # Trường hợp Left Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)  # Trường hợp Right Right
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)  # Trường hợp Right Left

        return root  # Trả về nút đã được cân bằng lại

    # Hàm tìm kiếm một giá trị trong cây AVL
    def find(self, root, key):
        if root is None or root.key == key:
            return root  # Nếu cây rỗng hoặc tìm thấy giá trị, trả về nút hiện tại

        if key < root.key:
            return self.find(root.left, key)  # Tìm kiếm trong cây con bên trái

        return self.find(root.right, key)  # Tìm kiếm trong cây con bên phải

    # Hàm sửa đổi giá trị của một nút trong cây AVL
    def update(self, root, old_key, new_key):
        root = self.delete(root, old_key)  # Xóa nút có giá trị cũ
        root = self.insert(root, new_key)  # Chèn nút có giá trị mới
        return root

    # Hàm tìm nút có giá trị nhỏ nhất trong cây
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    # Hàm thực hiện xoay trái
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    # Hàm thực hiện xoay phải
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    # Hàm lấy chiều cao của một nút
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Hàm lấy hệ số cân bằng của một nút
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # Hàm duyệt cây theo thứ tự trước (PreOrder)
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Hàm duyệt cây theo thứ tự trung (InOrder)
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.key), end="")
        self.inOrder(root.right)

    # Hàm duyệt cây theo thứ tự sau (PostOrder)
    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print("{0} ".format(root.key), end="")


# Khởi tạo cây AVL
tree = AVLTree()
root = None

# Thêm các phần tử vào cây AVL
keys_to_insert = [10, 20, 30, 40, 50, 25]
for key in keys_to_insert:
    root = tree.insert(root, key)

# In cây theo thứ tự trước (PreOrder)
print("Cây sau khi thêm các phần tử (PreOrder):")
tree.preOrder(root)
print("\n")

# In cây theo thứ tự trung (InOrder)
print("Cây sau khi thêm các phần tử (InOrder):")
tree.inOrder(root)
print("\n")

# In cây theo thứ tự sau (PostOrder)
print("Cây sau khi thêm các phần tử (PostOrder):")
tree.postOrder(root)
print("\n")

# Tìm kiếm một phần tử trong cây AVL
key_to_find = 30
result = tree.find(root, key_to_find)
if result:
    print(f"Tìm thấy phần tử {key_to_find} trong cây.\n")
else:
    print(f"Không tìm thấy phần tử {key_to_find} trong cây.\n")

# Sửa đổi một phần tử trong cây AVL
old_key = 30
new_key = 35
root = tree.update(root, old_key, new_key)

# In cây theo thứ tự trước (PreOrder) sau khi sửa đổi phần tử
print(f"Cây sau khi sửa đổi phần tử {old_key} thành {new_key} (PreOrder):")
tree.preOrder(root)
print("\n")

# Xóa một phần tử khỏi cây AVL
key_to_delete = 20
root = tree.delete(root, key_to_delete)

# In cây theo thứ tự trước (PreOrder) sau khi xóa phần tử
print(f"Cây sau khi xóa phần tử {key_to_delete} (PreOrder):")
tree.preOrder(root)
print("\n")

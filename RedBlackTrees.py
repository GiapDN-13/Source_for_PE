class Node:
    def __init__(self, key):
        self.key = key  # Khóa của nút
        self.left = None  # Con trỏ tới cây con bên trái
        self.right = None  # Con trỏ tới cây con bên phải

class SplayTree:
    def __init__(self):
        self.root = None  # Gốc của cây splay

    # Hàm xoay phải
    def _right_rotate(self, x):
        y = x.left  # y là cây con bên trái của x
        x.left = y.right  # Cây con bên phải của y trở thành cây con bên trái của x
        y.right = x  # x trở thành cây con bên phải của y
        return y  # Trả về y là gốc của cây sau khi xoay

    # Hàm xoay trái
    def _left_rotate(self, x):
        y = x.right  # y là cây con bên phải của x
        x.right = y.left  # Cây con bên trái của y trở thành cây con bên phải của x
        y.left = x  # x trở thành cây con bên trái của y
        return y  # Trả về y là gốc của cây sau khi xoay

    # Hàm splay để đưa node có key lên gốc
    def _splay(self, root, key):
        if root is None or root.key == key:
            return root  # Trả về root nếu root rỗng hoặc root đã là node cần tìm

        # Key nằm ở cây con bên trái
        if key < root.key:
            if root.left is None:
                return root  # Trả về root nếu cây con bên trái rỗng

            # Zig-Zig (Left Left)
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)  # Splay cây con bên trái của cây con bên trái
                root = self._right_rotate(root)  # Xoay phải

            # Zig-Zag (Left Right)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)  # Splay cây con bên phải của cây con bên trái
                if root.left.right is not None:
                    root.left = self._left_rotate(root.left)  # Xoay trái cây con bên trái

            return root if root.left is None else self._right_rotate(root)  # Xoay phải và trả về root mới

        # Key nằm ở cây con bên phải
        else:
            if root.right is None:
                return root  # Trả về root nếu cây con bên phải rỗng

            # Zag-Zig (Right Left)
            if key < root.right.key:
                root.right.left = self._splay(root.right.left, key)  # Splay cây con bên trái của cây con bên phải
                if root.right.left is not None:
                    root.right = self._right_rotate(root.right)  # Xoay phải cây con bên phải

            # Zag-Zag (Right Right)
            elif key > root.right.key:
                root.right.right = self._splay(root.right.right, key)  # Splay cây con bên phải của cây con bên phải
                root = self._left_rotate(root)  # Xoay trái

            return root if root.right is None else self._left_rotate(root)  # Xoay trái và trả về root mới

    # Hàm tìm kiếm
    def search(self, key):
        self.root = self._splay(self.root, key)  # Splay cây với key
        return self.root is not None and self.root.key == key  # Trả về True nếu tìm thấy key, ngược lại False

    # Hàm chèn
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # Nếu cây rỗng, tạo node mới làm gốc
            return

        self.root = self._splay(self.root, key)  # Splay cây với key

        if self.root.key == key:
            return  # Nếu key đã tồn tại, không chèn thêm

        new_node = Node(key)  # Tạo node mới với key
        if key < self.root.key:
            new_node.right = self.root  # Node mới trở thành gốc, root cũ trở thành cây con bên phải của node mới
            new_node.left = self.root.left  # Cây con bên trái của root cũ trở thành cây con bên trái của node mới
            self.root.left = None  # Cắt liên kết cây con bên trái của root cũ
        else:
            new_node.left = self.root  # Node mới trở thành gốc, root cũ trở thành cây con bên trái của node mới
            new_node.right = self.root.right  # Cây con bên phải của root cũ trở thành cây con bên phải của node mới
            self.root.right = None  # Cắt liên kết cây con bên phải của root cũ

        self.root = new_node  # Cập nhật root thành node mới

    # Hàm xóa
    def delete(self, key):
        if self.root is None:
            return  # Nếu cây rỗng, không làm gì cả

        self.root = self._splay(self.root, key)  # Splay cây với key

        if self.root.key != key:
            return  # Nếu key không tồn tại, không làm gì cả

        if self.root.left is None:
            self.root = self.root.right  # Nếu cây con bên trái rỗng, cập nhật root thành cây con bên phải
        elif self.root.right is None:
            self.root = self.root.left  # Nếu cây con bên phải rỗng, cập nhật root thành cây con bên trái
        else:
            temp = self.root  # Lưu lại root hiện tại
            self.root = self._splay(self.root.left, key)  # Splay cây con bên trái với key
            self.root.right = temp.right  # Cập nhật cây con bên phải của root mới

    # Hàm sửa
    def update(self, old_key, new_key):
        self.root = self._splay(self.root, old_key)  # Splay cây với old_key
        if self.root is None or self.root.key != old_key:
            return False  # Nếu không tìm thấy old_key, trả về False

        self.delete(old_key)  # Xóa nút có khóa old_key
        self.insert(new_key)  # Chèn nút mới với khóa new_key
        return True  # Trả về True nếu sửa thành công

    # Hàm duyệt cây theo thứ tự trước (preorder)
    def _preorder_helper(self, root):
        if root is not None:
            print(root.key, end=' ')  # In key của node hiện tại
            self._preorder_helper(root.left)  # Duyệt cây con bên trái
            self._preorder_helper(root.right)  # Duyệt cây con bên phải

    def preorder(self):
        self._preorder_helper(self.root)  # Gọi hàm preorder helper với gốc cây
        print()  # In dòng mới sau khi in xong cây

    # Hàm duyệt cây theo thứ tự giữa (inorder)
    def _inorder_helper(self, root):
        if root is not None:
            self._inorder_helper(root.left)  # Duyệt cây con bên trái
            print(root.key, end=' ')  # In key của node hiện tại
            self._inorder_helper(root.right)  # Duyệt cây con bên phải

    def inorder(self):
        self._inorder_helper(self.root)  # Gọi hàm inorder helper với gốc cây
        print()  # In dòng mới sau khi in xong cây

    # Hàm duyệt cây theo thứ tự sau (postorder)
    def _postorder_helper(self, root):
        if root is not None:
            self._postorder_helper(root.left)  # Duyệt cây con bên trái
            self._postorder_helper(root.right)  # Duyệt cây con bên phải
            print(root.key, end=' ')  # In key của node hiện tại

    def postorder(self):
        self._postorder_helper(self.root)  # Gọi hàm postorder helper với gốc cây
        print()  # In dòng mới sau khi in xong cây

    # Hàm duyệt cây theo tầng (level-order)
    def level_order(self):
        if self.root is None:
            return  # Nếu cây rỗng, không làm gì cả

        queue = []  # Tạo hàng đợi để lưu các node
        queue.append(self.root)  # Thêm gốc cây vào hàng đợi

        while queue:
            current = queue.pop(0)  # Lấy node đầu tiên ra khỏi hàng đợi
            print(current.key, end=' ')  # In key của node hiện tại

            if current.left is not None:
                queue.append(current.left)  # Thêm cây con bên trái vào hàng đợi

            if current.right is not None:
                queue.append(current.right)  # Thêm cây con bên phải vào hàng đợi

        print()  # In dòng mới sau khi in xong cây

# Tạo cây splay tree
tree = SplayTree()

# Chèn các phần tử vào cây
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

# In cây theo thứ tự giữa
print("Cây sau khi chèn:")
tree.inorder()

# Tìm kiếm một phần tử
key = 30
found = tree.search(key)
print(f"Tìm kiếm {key}: {'Tìm thấy' if found else 'Không tìm thấy'}")

# Xóa một phần tử
tree.delete(20)
print("Cây sau khi xóa 20:")
tree.inorder()

# Tìm kiếm một phần tử không tồn tại
key = 60
found = tree.search(key)
print(f"Tìm kiếm {key}: {'Tìm thấy' if found else 'Không tìm thấy'}")

# Sửa một phần tử
tree.update(30, 35)
print("Cây sau khi sửa 30 thành 35:")
tree.inorder()

# In cây theo thứ tự trước
print("Duyệt cây theo thứ tự trước:")
tree.preorder()

# In cây theo thứ tự sau
print("Duyệt cây theo thứ tự sau:")
tree.postorder()

# In cây theo tầng
print("Duyệt cây theo tầng:")
tree.level_order()

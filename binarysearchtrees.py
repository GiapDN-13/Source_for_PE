class Node:
    """Lớp Node biểu diễn một nút trong cây nhị phân tìm kiếm"""

    def __init__(self, key):
        self.left = None  # Con trái của nút
        self.right = None  # Con phải của nút
        self.val = key  # Giá trị của nút


class BinarySearchTree:
    """Lớp BinarySearchTree biểu diễn cây nhị phân tìm kiếm"""

    def __init__(self):
        self.root = None  # Gốc của cây

    def insert(self, key):
        """Hàm chèn một giá trị vào cây"""
        if self.root is None:
            self.root = Node(key)  # Nếu cây rỗng, tạo nút gốc
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """Hàm đệ quy chèn giá trị vào đúng vị trí"""
        if key == node.val:
            return  # Không cho phép chèn giá trị trùng lặp
        if key < node.val:
            if node.left is None:
                node.left = Node(key)  # Nếu không có con trái, tạo nút mới
            else:
                self._insert(node.left, key)  # Nếu có con trái, tiếp tục chèn vào cây con trái
        else:
            if node.right is None:
                node.right = Node(key)  # Nếu không có con phải, tạo nút mới
            else:
                self._insert(node.right, key)  # Nếu có con phải, tiếp tục chèn vào cây con phải

    def search(self, key):
        """Hàm tìm kiếm một giá trị trong cây"""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Hàm đệ quy tìm kiếm giá trị"""
        if node is None or node.val == key:
            return node  # Trả về nút nếu tìm thấy hoặc cây rỗng
        if key < node.val:
            return self._search(node.left, key)  # Tìm kiếm ở cây con trái
        return self._search(node.right, key)  # Tìm kiếm ở cây con phải

    def delete(self, key):
        """Hàm xóa một giá trị khỏi cây"""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Hàm đệ quy xóa giá trị"""
        if node is None:
            return node  # Trả về nếu cây rỗng
        if key < node.val:
            node.left = self._delete(node.left, key)  # Xóa ở cây con trái
        elif key > node.val:
            node.right = self._delete(node.right, key)  # Xóa ở cây con phải
        else:
            if node.left is None:
                return node.right  # Nút không có con trái
            elif node.right is None:
                return node.left  # Nút không có con phải
            temp = self._min_value_node(node.right)  # Nút có hai con, tìm nút nhỏ nhất ở cây con phải
            node.val = temp.val  # Thay giá trị của nút cần xóa bằng giá trị của nút nhỏ nhất
            node.right = self._delete(node.right, temp.val)  # Xóa nút nhỏ nhất ở cây con phải
        return node

    def _min_value_node(self, node):
        """Hàm tìm nút có giá trị nhỏ nhất trong cây"""
        current = node
        while current.left is not None:
            current = current.left  # Đi tới nút con trái cuối cùng
        return current

    def inorder_traversal(self):
        """Hàm duyệt cây theo thứ tự trung bình (inorder)"""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """Hàm đệ quy duyệt cây theo thứ tự trung bình"""
        if node:
            self._inorder_traversal(node.left, result)  # Duyệt cây con trái
            result.append(node.val)  # Thêm giá trị của nút vào kết quả
            self._inorder_traversal(node.right, result)  # Duyệt cây con phải

    def preorder_traversal(self):
        """Hàm duyệt cây theo thứ tự trước (preorder)"""
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        """Hàm đệ quy duyệt cây theo thứ tự trước"""
        if node:
            result.append(node.val)  # Thêm giá trị của nút vào kết quả
            self._preorder_traversal(node.left, result)  # Duyệt cây con trái
            self._preorder_traversal(node.right, result)  # Duyệt cây con phải

    def postorder_traversal(self):
        """Hàm duyệt cây theo thứ tự sau (postorder)"""
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        """Hàm đệ quy duyệt cây theo thứ tự sau"""
        if node:
            self._postorder_traversal(node.left, result)  # Duyệt cây con trái
            self._postorder_traversal(node.right, result)  # Duyệt cây con phải
            result.append(node.val)  # Thêm giá trị của nút vào kết quả

    def update(self, old_key, new_key):
        """Hàm cập nhật giá trị của một nút"""
        # Tìm nút cần cập nhật
        node = self.search(old_key)
        if node:
            self.delete(old_key)  # Xóa nút cũ
            self.insert(new_key)  # Chèn nút mới

# Sử dụng các chức năng CRUD và các hàm duyệt cây khác nhau
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# In ra kết quả duyệt cây theo thứ tự trung bình
print("Duyệt cây theo thứ tự trung bình (inorder traversal):", bst.inorder_traversal())

# In ra kết quả duyệt cây theo thứ tự trước
print("Duyệt cây theo thứ tự trước (preorder traversal):", bst.preorder_traversal())

# In ra kết quả duyệt cây theo thứ tự sau
print("Duyệt cây theo thứ tự sau (postorder traversal):", bst.postorder_traversal())

# Tìm kiếm các giá trị
print("Tìm kiếm 40:", bst.search(40) is not None)
print("Tìm kiếm 90:", bst.search(90) is not None)

# Xóa các giá trị và in ra kết quả sau mỗi lần xóa
bst.delete(20)
print("Cây sau khi xóa 20:", bst.inorder_traversal())

bst.delete(30)
print("Cây sau khi xóa 30:", bst.inorder_traversal())

bst.delete(50)
print("Cây sau khi xóa 50:", bst.inorder_traversal())

# Cập nhật giá trị của một nút
bst.update(40, 45)
print("Cây sau khi cập nhật 40 thành 45:", bst.inorder_traversal())

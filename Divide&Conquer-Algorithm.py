class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class DivideAndConquer:
    def __init__(self):
        # Khởi tạo danh sách rỗng để lưu trữ các số cần sắp xếp
        self.data = []
        self.root = None

    def create(self, value):
        # Thêm một giá trị vào danh sách
        self.data.append(value)
        print(f"Đã thêm {value} vào danh sách.")

    def read(self):
        # Đọc và trả về danh sách hiện tại
        return self.data

    def update(self, index, value):
        # Cập nhật giá trị tại một vị trí cụ thể trong danh sách
        if 0 <= index < len(self.data):
            old_value = self.data[index]
            self.data[index] = value
            print(f"Đã cập nhật vị trí {index} từ {old_value} thành {value}.")
        else:
            print("Chỉ số không hợp lệ.")

    def delete(self, index):
        # Xóa giá trị tại một vị trí cụ thể trong danh sách
        if 0 <= index < len(self.data):
            removed_value = self.data.pop(index)
            print(f"Đã xóa {removed_value} từ vị trí {index}.")
        else:
            print("Chỉ số không hợp lệ.")

    def merge_sort(self, data=None):
        # Sắp xếp danh sách bằng thuật toán Merge Sort (sắp xếp trộn)
        if data is None:
            data = self.data

        if len(data) > 1:
            mid = len(data) // 2  # Tìm điểm giữa của danh sách
            left_half = data[:mid]  # Chia danh sách thành nửa bên trái
            right_half = data[mid:]  # Chia danh sách thành nửa bên phải

            self.merge_sort(left_half)  # Đệ quy sắp xếp nửa bên trái
            self.merge_sort(right_half)  # Đệ quy sắp xếp nửa bên phải

            i = j = k = 0

            # Trộn hai nửa đã được sắp xếp vào danh sách kết quả
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            # Xử lý phần còn lại của nửa bên trái
            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            # Xử lý phần còn lại của nửa bên phải
            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data

    def add_to_bst(self, value):
        # Thêm một giá trị vào cây nhị phân tìm kiếm
        if not self.root:
            self.root = Node(value)
        else:
            self._add_to_bst(self.root, value)

    def _add_to_bst(self, node, value):
        # Hàm đệ quy để thêm một giá trị vào cây nhị phân tìm kiếm
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_to_bst(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_to_bst(node.right, value)

    def preorder_traversal(self):
        # Duyệt cây theo thứ tự trước (preorder)
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        # Hàm đệ quy để duyệt cây theo thứ tự trước (preorder)
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def inorder_traversal(self):
        # Duyệt cây theo thứ tự giữa (inorder)
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        # Hàm đệ quy để duyệt cây theo thứ tự giữa (inorder)
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def postorder_traversal(self):
        # Duyệt cây theo thứ tự sau (postorder)
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        # Hàm đệ quy để duyệt cây theo thứ tự sau (postorder)
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)

# Ví dụ sử dụng lớp DivideAndConquer
dac = DivideAndConquer()

# Thêm các giá trị vào danh sách
dac.create(3)
dac.create(1)
dac.create(4)
dac.create(1)
dac.create(5)

# Đọc danh sách hiện tại
print("Danh sách hiện tại:", dac.read())

# Cập nhật một giá trị trong danh sách
dac.update(2, 9)

# Xóa một giá trị khỏi danh sách
dac.delete(3)

# Đọc danh sách hiện tại sau khi cập nhật và xóa
print("Danh sách sau khi cập nhật và xóa:", dac.read())

# Sắp xếp danh sách bằng Merge Sort
sorted_data = dac.merge_sort()
print("Danh sách đã được sắp xếp:", sorted_data)

# Thêm các giá trị vào cây nhị phân tìm kiếm
dac.add_to_bst(3)
dac.add_to_bst(1)
dac.add_to_bst(4)
dac.add_to_bst(1)
dac.add_to_bst(5)

# Duyệt cây theo thứ tự trước (preorder)
print("Duyệt cây theo thứ tự trước (preorder):", dac.preorder_traversal())

# Duyệt cây theo thứ tự giữa (inorder)
print("Duyệt cây theo thứ tự giữa (inorder):", dac.inorder_traversal())

# Duyệt cây theo thứ tự sau (postorder)
print("Duyệt cây theo thứ tự sau (postorder):", dac.postorder_traversal())

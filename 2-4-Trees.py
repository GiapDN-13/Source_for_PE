class Node:
    def __init__(self):
        # Khởi tạo node với danh sách keys and children rỗng
        self.keys = []
        self.children = []

    def is_leaf(self):
        # Kiểm tra xem node có phải là lá (không có children) không
        return len(self.children) == 0

    def is_full(self):
        # Kiểm tra xem node có đầy (có 3 keys) không
        return len(self.keys) == 3

    def insert_non_full(self, key):
        # Chèn key ando node chưa đầy
        if self.is_leaf():
            # Nếu node là lá, chèn key ando đúng vị trí
            self.keys.append(key)
            self.keys.sort()
        else:
            # Nếu node không phải là lá, tìm child phù hợp để chèn key
            i = 0
            while i < len(self.keys) and key > self.keys[i]:
                i += 1
            # Nếu child i đã đầy, phân chia child đó
            if self.children[i].is_full():
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            # Chèn key ando child thích hợp
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        # Phân chia child i đầy thành hai children
        full_child = self.children[i]
        new_child = Node()

        # Chia keys and children của full_child
        self.keys.insert(i, full_child.keys[1])
        self.children.insert(i + 1, new_child)

        new_child.keys = full_child.keys[2:]
        full_child.keys = full_child.keys[:1]

        if not full_child.is_leaf():
            new_child.children = full_child.children[2:]
            full_child.children = full_child.children[:2]

    def remove(self, key):
        # Xóa key từ node
        if key in self.keys:
            # Nếu key có trong node
            if self.is_leaf():
                # Nếu node là lá, đơn giản xóa key
                self.keys.remove(key)
            else:
                # Nếu không phải lá, thay thế key bằng predecessor hoặc successor
                idx = self.keys.index(key)
                if len(self.children[idx].keys) > 1:
                    predecessor = self.children[idx].get_predecessor()
                    self.keys[idx] = predecessor
                    self.children[idx].remove(predecessor)
                elif len(self.children[idx + 1].keys) > 1:
                    successor = self.children[idx + 1].get_successor()
                    self.keys[idx] = successor
                    self.children[idx + 1].remove(successor)
                else:
                    # Nếu cả hai child đều có 1 key, hợp nhất child and child kế tiếp
                    self.merge(idx)
                    self.children[idx].remove(key)
        else:
            # Nếu key không có trong node
            if self.is_leaf():
                return
            # Tìm child thích hợp để xóa key
            idx = 0
            while idx < len(self.keys) and key > self.keys[idx]:
                idx += 1
            if len(self.children[idx].keys) == 1:
                # Nếu child có 1 key, mượn key từ child khác hoặc hợp nhất
                if idx > 0 and len(self.children[idx - 1].keys) > 1:
                    self.borrow_from_prev(idx)
                elif idx < len(self.keys) and len(self.children[idx + 1].keys) > 1:
                    self.borrow_from_next(idx)
                else:
                    if idx < len(self.keys):
                        self.merge(idx)
                    else:
                        self.merge(idx - 1)
            # Tiếp tục xóa key từ child thích hợp
            self.children[idx].remove(key)

    def get_predecessor(self):
        # Lấy phần tử tiền nhiệm (lớn nhất trong cây con bên trái)
        if self.is_leaf():
            return self.keys[-1]
        else:
            return self.children[-1].get_predecessor()

    def get_successor(self):
        # Lấy phần tử kế nhiệm (nhỏ nhất trong cây con bên phải)
        if self.is_leaf():
            return self.keys[0]
        else:
            return self.children[0].get_successor()

    def borrow_from_prev(self, idx):
        # Mượn key từ child trước đó
        child = self.children[idx]
        sibling = self.children[idx - 1]

        child.keys.insert(0, self.keys[idx - 1])
        if not sibling.is_leaf():
            child.children.insert(0, sibling.children.pop())

        self.keys[idx - 1] = sibling.keys.pop()

    def borrow_from_next(self, idx):
        # Mượn key từ child kế tiếp
        child = self.children[idx]
        sibling = self.children[idx + 1]

        child.keys.append(self.keys[idx])
        if not sibling.is_leaf():
            child.children.append(sibling.children.pop(0))

        self.keys[idx] = sibling.keys.pop(0)

    def merge(self, idx):
        # Hợp nhất child với child kế tiếp
        child = self.children[idx]
        sibling = self.children.pop(idx + 1)

        child.keys.append(self.keys.pop(idx))
        child.keys.extend(sibling.keys)
        child.children.extend(sibling.children)


class TwoFourTree:
    def __init__(self):
        # Khởi tạo cây với một root là node rỗng
        self.root = Node()

    def insert(self, key):
        # Hàm chèn một key ando cây
        if self.root.is_full():
            # Nếu root đầy, tạo node mới and chia root cũ thành 2 children
            new_root = Node()
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root
        # Chèn key ando cây
        self.root.insert_non_full(key)

    def find(self, key, node=None):
        # Hàm tìm kiếm một key trong cây
        if node is None:
            node = self.root
        if key in node.keys:
            # Nếu key có trong node hiện tại
            return True
        elif node.is_leaf():
            # Nếu node là lá and key không có trong node
            return False
        else:
            # Nếu không phải lá, tiếp tục tìm kiếm trong child thích hợp
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return self.find(key, node.children[i])

    def delete(self, key):
        # Hàm xóa một key khỏi cây
        if not self.root:
            return

        self.root.remove(key)

        # Nếu root rỗng sau khi xóa
        if len(self.root.keys) == 0:
            if not self.root.is_leaf():
                # Nếu root không phải lá, gán root mới là child đầu tiên
                self.root = self.root.children[0]
            else:
                # Nếu root là lá, gán root là None
                self.root = None

    def update(self, old_key, new_key):
        # Hàm cập nhật một key trong cây
        if self.find(old_key):
            self.delete(old_key)
            self.insert(new_key)
            return True
        return False

    def print_tree(self, node=None, level=0):
        # Hàm in cây ra màn hình (dùng đệ quy)
        if node is None:
            node = self.root
        print("Level", level, "Keys:", node.keys)
        level += 1
        for child in node.children:
            self.print_tree(child, level)

    def preorder(self, node=None):
        # Duyệt cây theo thứ tự trước (NLR: Node-Left-Right)
        if node is None:
            node = self.root
        result = []
        result.extend(node.keys)
        for child in node.children:
            result.extend(self.preorder(child))
        return result

    def inorder(self, node=None):
        # Duyệt cây theo thứ tự giữa (LNR: Left-Node-Right)
        if node is None:
            node = self.root
        result = []
        for i in range(len(node.keys)):
            if i < len(node.children):
                result.extend(self.inorder(node.children[i]))
            result.append(node.keys[i])
        if len(node.children) > len(node.keys):
            result.extend(self.inorder(node.children[-1]))
        return result

    def postorder(self, node=None):
        # Duyệt cây theo thứ tự sau (LRN: Left-Right-Node)
        if node is None:
            node = self.root
        result = []
        for child in node.children:
            result.extend(self.postorder(child))
        result.extend(node.keys)
        return result


# Sử dụng các chức năng CRUD

# Khởi tạo cây
tree = TwoFourTree()

# Chèn các phần tử ando cây
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(6)
tree.insert(12)
tree.insert(30)
tree.insert(7)
tree.insert(17)

# Tìm kiếm phần tử trong cây
print(tree.find(10))  # Output: True
print(tree.find(15))  # Output: False

# In cây ra màn hình
print("Cây sau khi chèn:")
tree.print_tree()

# Cập nhật một phần tử trong cây
print("Cập nhật 6 thành 16")
tree.update(6, 16)

# In cây sau khi cập nhật
print("Cây sau khi cập nhật:")
tree.print_tree()

# Xóa phần tử khỏi cây
print("Xóa 16 and 30 khỏi cây")
tree.delete(16)
tree.delete(30)

# In cây sau khi xóa
print("Cây sau khi xóa:")
tree.print_tree()

# Duyệt cây theo thứ tự trước (preorder)
print("Duyệt cây theo thứ tự trước:")
print(tree.preorder())

# Duyệt cây theo thứ tự giữa (inorder)
print("Duyệt cây theo thứ tự giữa:")
print(tree.inorder())

# Duyệt cây theo thứ tự sau (postorder)
print("Duyệt cây theo thứ tự sau:")
print(tree.postorder())

import random

# Định nghĩa node trong skiplist
class Node:
    def __init__(self, value, level):
        self.value = value  # Giá trị của node
        self.forward = [None] * (level + 1)  # Danh sách các con trỏ forward tới các node ở các level khác nhau

# Định nghĩa skiplist
class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level  # Level tối đa của skiplist
        self.p = p  # Xác suất để quyết định level của node
        self.header = self.create_node(self.max_level, -1)  # Node header
        self.level = 0  # Level hiện tại của skiplist

    # Tạo một node mới
    def create_node(self, lvl, value):
        node = Node(value, lvl)
        return node

    # Tạo một level ngẫu nhiên cho node
    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    # Chèn một giá trị vào skiplist
    def insert_element(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        # Di chuyển node hiện tại đến vị trí cần chèn
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        # Chèn node mới
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl

        new_node = self.create_node(lvl, value)
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    # Tìm kiếm một giá trị trong skiplist
    def search_element(self, value):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return True
        return False

    # Xóa một giá trị trong skiplist
    def delete_element(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        # Di chuyển node hiện tại đến vị trí cần xóa
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        # Xóa node
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Điều chỉnh lại level của skiplist nếu cần
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    # Cập nhật một giá trị trong skiplist
    def update_element(self, old_value, new_value):
        if self.search_element(old_value):
            self.delete_element(old_value)
            self.insert_element(new_value)
            return True
        return False

# Khởi tạo skiplist với level tối đa là 3 và xác suất là 0.5
skiplist = SkipList(3, 0.5)

# Thêm các phần tử vào skiplist
skiplist.insert_element(3)
skiplist.insert_element(6)
skiplist.insert_element(7)
skiplist.insert_element(9)
skiplist.insert_element(12)
skiplist.insert_element(19)
skiplist.insert_element(17)
skiplist.insert_element(26)
skiplist.insert_element(21)

# Tìm kiếm các phần tử trong skiplist
print(skiplist.search_element(19))  # Output: True
print(skiplist.search_element(15))  # Output: False

# Cập nhật phần tử trong skiplist
print(skiplist.update_element(19, 22))  # Output: True
print(skiplist.search_element(19))  # Output: False
print(skiplist.search_element(22))  # Output: True

# Xóa phần tử trong skiplist
skiplist.delete_element(22)
print(skiplist.search_element(22))  # Output: False

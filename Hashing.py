class HashTable:
    def __init__(self, size):
        # Khởi tạo bảng băm với kích thước cho trước
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        # Hàm băm đơn giản: sử dụng độ dài của chuỗi khóa
        return len(key) % self.size

    def insert(self, key, value):
        # Thêm cặp khóa-giá trị vào bảng băm
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        # Thêm cặp khóa-giá trị vào danh sách tại vị trí index
        self.table[index].append((key, value))

    def search(self, key):
        # Tìm kiếm giá trị dựa trên khóa
        index = self._hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None  # Trả về None nếu không tìm thấy khóa

    def delete(self, key):
        # Xóa cặp khóa-giá trị dựa trên khóa
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return True
        return False  # Trả về False nếu không tìm thấy khóa

    def update(self, key, new_value):
        # Cập nhật giá trị cho khóa đã tồn tại
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, new_value)
                    return True
        return False  # Trả về False nếu không tìm thấy khóa để cập nhật


# Ví dụ sử dụng HashTable
if __name__ == "__main__":
    # Tạo bảng băm với kích thước 10
    hash_table = HashTable(10)

    # Thêm một số cặp khóa-giá trị vào bảng
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("grape", 3)

    # Tìm kiếm giá trị dựa trên khóa
    print("Value for 'apple':", hash_table.search("apple"))  # Output: 1
    print("Value for 'banana':", hash_table.search("banana"))  # Output: 2
    print("Value for 'grape':", hash_table.search("grape"))  # Output: 3
    print("Value for 'pear':", hash_table.search("pear"))  # Output: None

    # Cập nhật giá trị cho khóa 'banana'
    hash_table.update("banana", 5)
    print("Updated value for 'banana':", hash_table.search("banana"))  # Output: 5

    # Xóa một cặp khóa-giá trị
    hash_table.delete("banana")
    print("Value for 'banana' after deletion:", hash_table.search("banana"))  # Output: None

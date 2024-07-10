class DoubleHashingHashTable:
    def __init__(self, table_size):
        # Khởi tạo bảng băm với kích thước cho trước
        self.table_size = table_size
        self.hash_table = [None] * table_size  # Khởi tạo bảng với các giá trị None
        self.element_count = 0  # Số lượng phần tử hiện có trong bảng băm

    def is_full(self):
        # Kiểm tra xem bảng băm đã đầy hay chưa
        return self.element_count == self.table_size

    def primary_hash(self, key):
        # Hàm băm chính (ví dụ: sử dụng phép chia lấy dư)
        return key % self.table_size

    def secondary_hash(self, key):
        # Hàm băm phụ (phải khác 0 và khác hàm băm chính)
        # Một lựa chọn phổ biến là sử dụng một số nguyên tố nhỏ hơn kích thước bảng
        return 1 + (key % (self.table_size - 1))

    def insert(self, key, value):
        if self.is_full():
            raise Exception("Bảng băm đã đầy")

        # Lấy chỉ số ban đầu từ hàm băm chính
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)

        # Vòng lặp để tìm chỉ số đúng bằng băm kép
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                # Cập nhật giá trị nếu khóa đã tồn tại
                self.hash_table[index] = (key, value)
                return
            # Tính toán chỉ số mới
            index = (index + step_size) % self.table_size

        # Chèn cặp khóa-giá trị mới
        self.hash_table[index] = (key, value)
        self.element_count += 1

    def search(self, key):
        # Lấy chỉ số ban đầu từ hàm băm chính
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)

        # Vòng lặp để tìm chỉ số đúng bằng băm kép
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
            # Tính toán chỉ số mới
            index = (index + step_size) % self.table_size

        # Trả về None nếu không tìm thấy khóa
        return None

    def delete(self, key):
        # Lấy chỉ số ban đầu từ hàm băm chính
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)

        # Vòng lặp để tìm chỉ số đúng bằng băm kép
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                # Đánh dấu ô là đã bị xóa
                self.hash_table[index] = None
                self.element_count -= 1
                return True
            # Tính toán chỉ số mới
            index = (index + step_size) % self.table_size

        # Trả về False nếu không tìm thấy khóa
        return False


# Ví dụ sử dụng:
hash_table = DoubleHashingHashTable(10)

# Chèn các cặp khóa-giá trị
hash_table.insert(1, 'A')
hash_table.insert(11, 'B')
hash_table.insert(21, 'C')

# Tìm kiếm một khóa
print(hash_table.search(11))  # Kết quả: B

# Cập nhật một khóa
hash_table.insert(11, 'D')
print(hash_table.search(11))  # Kết quả: D

# Xóa một khóa
hash_table.delete(11)

# Thử tìm kiếm khóa đã bị xóa
print(hash_table.search(11))  # Kết quả: None

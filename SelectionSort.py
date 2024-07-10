class ListManager:
    def __init__(self):
        # Khởi tạo một danh sách rỗng
        self.data = []

    def add_item(self, item):
        # Thêm một phần tử vào danh sách
        self.data.append(item)

    def view_items(self):
        # Hiển thị tất cả các phần tử trong danh sách
        for item in self.data:
            print(item)

    def update_item(self, index, new_value):
        # Cập nhật giá trị của một phần tử tại vị trí chỉ định
        if 0 <= index < len(self.data):
            self.data[index] = new_value
        else:
            print("Index không hợp lệ")

    def delete_item(self, index):
        # Xoá một phần tử tại vị trí chỉ định
        if 0 <= index < len(self.data):
            self.data.pop(index)
        else:
            print("Index không hợp lệ")

    def find_item(self, item):
        # Tìm kiếm vị trí của một phần tử trong danh sách
        try:
            return self.data.index(item)
        except ValueError:
            return -1

    def selection_sort(self):
        # Sắp xếp danh sách sử dụng thuật toán Selection Sort
        n = len(self.data)
        for i in range(n):
            # Giả sử phần tử nhỏ nhất là phần tử đầu tiên
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]


# Tạo một đối tượng ListManager
manager = ListManager()

# Thêm các phần tử vào danh sách
manager.add_item(64)
manager.add_item(25)
manager.add_item(12)
manager.add_item(22)
manager.add_item(11)

# Hiển thị các phần tử trước khi sắp xếp
print("Danh sách trước khi sắp xếp:")
manager.view_items()

# Sắp xếp danh sách
manager.selection_sort()

# Hiển thị các phần tử sau khi sắp xếp
print("Danh sách sau khi sắp xếp:")
manager.view_items()

# Cập nhật phần tử tại vị trí chỉ định
manager.update_item(0, 100)

# Hiển thị danh sách sau khi cập nhật
print("Danh sách sau khi cập nhật:")
manager.view_items()

# Xoá phần tử tại vị trí chỉ định
manager.delete_item(1)

# Hiển thị danh sách sau khi xoá
print("Danh sách sau khi xoá:")
manager.view_items()

# Tìm kiếm vị trí của phần tử trong danh sách
index = manager.find_item(22)
if index != -1:
    print(f"Phần tử 22 được tìm thấy tại vị trí: {index}")
else:
    print("Phần tử 22 không tồn tại trong danh sách")

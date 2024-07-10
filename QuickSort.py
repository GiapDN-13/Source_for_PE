class QuickSortCRUD:
    def __init__(self):
        # Khởi tạo danh sách rỗng
        self.data = []

    def create(self, value):
        """Thêm một phần tử vào danh sách."""
        self.data.append(value)
        print(f"Đã thêm {value} vào danh sách.")

    def read(self):
        """Đọc và trả về danh sách hiện tại."""
        return self.data

    def update(self, index, value):
        """Cập nhật giá trị của phần tử tại vị trí index."""
        if 0 <= index < len(self.data):
            old_value = self.data[index]
            self.data[index] = value
            print(f"Đã cập nhật phần tử tại vị trí {index} từ {old_value} thành {value}.")
        else:
            print(f"Không tìm thấy phần tử tại vị trí {index}.")

    def delete(self, index):
        """Xóa phần tử tại vị trí index."""
        if 0 <= index < len(self.data):
            removed_value = self.data.pop(index)
            print(f"Đã xóa phần tử {removed_value} tại vị trí {index}.")
        else:
            print(f"Không tìm thấy phần tử tại vị trí {index}.")

    def partition(self, low, high):
        """Chia mảng thành hai phần dựa trên pivot."""
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1

    def quick_sort(self, low, high):
        """Thực hiện sắp xếp nhanh (QuickSort) trên danh sách."""
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def sort(self):
        """Hàm public để sắp xếp danh sách."""
        self.quick_sort(0, len(self.data) - 1)
        print("Danh sách đã được sắp xếp.")

    def search(self, value):
        """Tìm kiếm phần tử trong danh sách."""
        indices = [index for index, val in enumerate(self.data) if val == value]
        if indices:
            print(f"Phần tử {value} tìm thấy tại vị trí: {indices}")
            return indices
        else:
            print(f"Phần tử {value} không tìm thấy trong danh sách.")
            return []

# Sử dụng lớp QuickSortCRUD
qs = QuickSortCRUD()

# Thêm phần tử vào danh sách
qs.create(10)
qs.create(7)
qs.create(8)
qs.create(9)
qs.create(1)
qs.create(5)

# Đọc danh sách hiện tại
print("Danh sách hiện tại:", qs.read())

# Cập nhật phần tử
qs.update(0, 3)
print("Danh sách sau khi cập nhật:", qs.read())

# Xóa phần tử
qs.delete(2)
print("Danh sách sau khi xóa:", qs.read())

# Sắp xếp danh sách
qs.sort()
print("Danh sách sau khi sắp xếp:", qs.read())

# Tìm kiếm phần tử
qs.search(9)
qs.search(2)

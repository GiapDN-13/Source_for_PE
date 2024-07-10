class MergeSort:
    def __init__(self):
        # Khởi tạo một danh sách rỗng để chứa các phần tử
        self.array = []

    def create(self, element):
        # Thêm một phần tử vào danh sách
        self.array.append(element)
        print(f"Đã thêm phần tử {element} vào danh sách.")

    def read(self):
        # Đọc danh sách hiện tại
        print("Danh sách hiện tại:", self.array)
        return self.array

    def update(self, index, new_value):
        # Cập nhật một phần tử tại vị trí index bằng giá trị mới
        if 0 <= index < len(self.array):
            old_value = self.array[index]
            self.array[index] = new_value
            print(f"Đã cập nhật phần tử tại vị trí {index} từ {old_value} thành {new_value}.")
        else:
            print(f"Vị trí {index} không hợp lệ.")

    def delete(self, index):
        # Xóa một phần tử tại vị trí index
        if 0 <= index < len(self.array):
            removed_value = self.array.pop(index)
            print(f"Đã xóa phần tử {removed_value} tại vị trí {index}.")
        else:
            print(f"Vị trí {index} không hợp lệ.")

    def search(self, element):
        # Tìm kiếm một phần tử trong danh sách
        try:
            index = self.array.index(element)
            print(f"Phần tử {element} được tìm thấy tại vị trí {index}.")
            return index
        except ValueError:
            print(f"Phần tử {element} không có trong danh sách.")
            return -1

    def merge_sort(self):
        # Hàm để sắp xếp danh sách bằng thuật toán Merge Sort
        self.array = self._merge_sort_rec(self.array)
        print("Danh sách sau khi sắp xếp:", self.array)

    def _merge_sort_rec(self, array):
        # Hàm đệ quy để thực hiện Merge Sort
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left_half = self._merge_sort_rec(array[:mid])
        right_half = self._merge_sort_rec(array[mid:])
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        # Hàm để gộp hai danh sách con đã sắp xếp
        merged = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

# Sử dụng class MergeSort
merge_sort_instance = MergeSort()

# Thêm phần tử vào danh sách
merge_sort_instance.create(5)
merge_sort_instance.create(3)
merge_sort_instance.create(8)
merge_sort_instance.create(6)

# Đọc danh sách hiện tại
merge_sort_instance.read()

# Cập nhật một phần tử trong danh sách
merge_sort_instance.update(2, 7)

# Đọc danh sách sau khi cập nhật
merge_sort_instance.read()

# Xóa một phần tử trong danh sách
merge_sort_instance.delete(1)

# Đọc danh sách sau khi xóa
merge_sort_instance.read()

# Tìm kiếm phần tử trong danh sách
merge_sort_instance.search(7)

# Sắp xếp danh sách bằng thuật toán Merge Sort
merge_sort_instance.merge_sort()

# Tìm kiếm phần tử trong danh sách đã sắp xếp
merge_sort_instance.search(6)

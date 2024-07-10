class RadixSort:
    def __init__(self):
        # Khởi tạo danh sách rỗng
        self.array = []

    # Chức năng Create - Thêm phần tử vào danh sách
    def create(self, element):
        self.array.append(element)

    # Chức năng Read - Lấy danh sách hiện tại
    def read(self):
        return self.array

    # Chức năng Update - Cập nhật giá trị phần tử tại vị trí index
    def update(self, index, element):
        if 0 <= index < len(self.array):
            self.array[index] = element
        else:
            raise IndexError("Index không hợp lệ")

    # Chức năng Delete - Xóa phần tử tại vị trí index
    def delete(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index không hợp lệ")

    # Chức năng Search - Tìm kiếm phần tử trong danh sách
    def search(self, element):
        return element in self.array

    # Chức năng Sort - Thực hiện Radix Sort
    def sort(self):
        def counting_sort(exp):
            n = len(self.array)
            output = [0] * n  # Mảng kết quả
            count = [0] * 10  # Mảng đếm, chứa số đếm từ 0 đến 9

            # Lưu trữ số lần xuất hiện của các chữ số trong count[]
            for i in range(n):
                index = (self.array[i] // exp) % 10
                count[index] += 1

            # Thay đổi count[i] để count[i] chứa vị trí thực tế của chữ số trong output[]
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Xây dựng mảng output
            i = n - 1
            while i >= 0:
                index = (self.array[i] // exp) % 10
                output[count[index] - 1] = self.array[i]
                count[index] -= 1
                i -= 1

            # Sao chép mảng output vào self.array để self.array chứa các số đã sắp xếp theo chữ số hiện tại
            for i in range(len(self.array)):
                self.array[i] = output[i]

        # Tìm giá trị lớn nhất để biết số chữ số tối đa
        max_num = max(self.array)

        # Thực hiện Counting Sort cho mỗi chữ số, exp là 10^i với i là 0, 1, 2, ...
        exp = 1
        while max_num // exp > 0:
            counting_sort(exp)
            exp *= 10


# Khởi tạo đối tượng RadixSort
radix_sort = RadixSort()

# Thêm phần tử vào danh sách
radix_sort.create(170)
radix_sort.create(45)
radix_sort.create(75)
radix_sort.create(90)
radix_sort.create(802)
radix_sort.create(24)
radix_sort.create(2)
radix_sort.create(66)

# Đọc danh sách hiện tại
print("Danh sách ban đầu:", radix_sort.read())

# Cập nhật phần tử tại vị trí 1
radix_sort.update(1, 99)
print("Danh sách sau khi cập nhật phần tử tại vị trí 1:", radix_sort.read())

# Xóa phần tử tại vị trí 3
radix_sort.delete(3)
print("Danh sách sau khi xóa phần tử tại vị trí 3:", radix_sort.read())

# Tìm kiếm phần tử 75
print("Tìm kiếm phần tử 75:", radix_sort.search(75))

# Tìm kiếm phần tử 100
print("Tìm kiếm phần tử 100:", radix_sort.search(100))

# Sắp xếp danh sách
radix_sort.sort()
print("Danh sách sau khi sắp xếp:", radix_sort.read())

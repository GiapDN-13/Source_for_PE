class SortingLowerBound:
    def __init__(self):
        # Khởi tạo danh sách trống
        self.data = []

    def create(self, value):
        """
        Tạo và thêm phần tử vào danh sách.
        :param value: Giá trị cần thêm vào danh sách.
        """
        self.data.append(value)
        # Sắp xếp danh sách sau khi thêm phần tử mới
        self.data.sort()

    def read(self):
        """
        Xem toàn bộ danh sách.
        :return: Danh sách hiện tại.
        """
        return self.data

    def update(self, old_value, new_value):
        """
        Sửa giá trị của phần tử trong danh sách.
        :param old_value: Giá trị cũ cần sửa.
        :param new_value: Giá trị mới thay thế.
        :return: True nếu sửa thành công, False nếu không tìm thấy phần tử cần sửa.
        """
        if old_value in self.data:
            index = self.data.index(old_value)
            self.data[index] = new_value
            # Sắp xếp lại danh sách sau khi cập nhật giá trị
            self.data.sort()
            return True
        return False

    def delete(self, value):
        """
        Xóa phần tử khỏi danh sách.
        :param value: Giá trị cần xóa.
        :return: True nếu xóa thành công, False nếu không tìm thấy phần tử cần xóa.
        """
        if value in self.data:
            self.data.remove(value)
            return True
        return False

    def search(self, value):
        """
        Tìm kiếm phần tử trong danh sách.
        :param value: Giá trị cần tìm.
        :return: Vị trí của phần tử trong danh sách (index) hoặc -1 nếu không tìm thấy.
        """
        if value in self.data:
            return self.data.index(value)
        return -1

# Ví dụ sử dụng lớp SortingLowerBound
if __name__ == "__main__":
    slb = SortingLowerBound()

    # Tạo phần tử mới
    slb.create(5)
    slb.create(3)
    slb.create(8)
    print("Danh sách sau khi thêm phần tử:", slb.read())

    # Tìm kiếm phần tử
    print("Tìm kiếm giá trị 3:", slb.search(3))
    print("Tìm kiếm giá trị 7:", slb.search(7))

    # Sửa phần tử
    slb.update(3, 7)
    print("Danh sách sau khi cập nhật giá trị:", slb.read())

    # Xóa phần tử
    slb.delete(5)
    print("Danh sách sau khi xóa phần tử:", slb.read())

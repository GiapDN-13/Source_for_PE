class Stack:
    def __init__(self):
        # Khởi tạo stack bằng một danh sách rỗng
        self.items = []

    def is_empty(self):
        """
        Kiểm tra xem stack có rỗng không.
        Trả về True nếu stack rỗng, ngược lại trả về False.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Thêm một phần tử vào đỉnh của stack.

        Args:
            item: Phần tử cần thêm vào stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Loại bỏ và trả về phần tử ở đỉnh của stack.
        Trả về phần tử ở đỉnh stack nếu stack không rỗng, ngược lại trả về None.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def top(self):
        """
        Trả về phần tử ở đỉnh của stack nhưng không loại bỏ nó.
        Trả về phần tử ở đỉnh stack nếu stack không rỗng, ngược lại trả về None.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """
        Trả về số lượng phần tử trong stack.
        """
        return len(self.items)

    def __str__(self):
        """
        Trả về biểu diễn chuỗi của stack.
        """
        return str(self.items)

    def read(self, index):
        """
        Đọc giá trị của phần tử tại một vị trí cụ thể trong stack.

        Args:
            index: Vị trí của phần tử cần đọc.

        Returns:
            Giá trị của phần tử tại vị trí index nếu tồn tại, ngược lại trả về None.
        """
        if 0 <= index < self.size():
            return self.items[index]
        return None

    def update(self, index, value):
        """
        Cập nhật giá trị của phần tử tại một vị trí cụ thể trong stack.

        Args:
            index: Vị trí của phần tử cần cập nhật.
            value: Giá trị mới của phần tử.

        Returns:
            True nếu cập nhật thành công, ngược lại trả về False.
        """
        if 0 <= index < self.size():
            self.items[index] = value
            return True
        return False

    def delete(self, index):
        """
        Xóa phần tử tại một vị trí cụ thể trong stack.

        Args:
            index: Vị trí của phần tử cần xóa.

        Returns:
            Giá trị của phần tử đã bị xóa nếu xóa thành công, ngược lại trả về None.
        """
        if 0 <= index < self.size():
            return self.items.pop(index)
        return None


# Ví dụ sử dụng lớp Stack
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack hiện tại:", stack)
    print("Phần tử trên đỉnh:", stack.top())
    print("Kích thước stack:", stack.size())

    stack.pop()
    print("Stack sau khi pop:", stack)
    print("Phần tử trên đỉnh:", stack.top())
    print("Kích thước stack:", stack.size())

    # Ví dụ CRUD
    #Create (Thêm mới):
    stack.push(4)
    stack.push(5)
    print("Stack sau khi push 4 và 5:", stack)
    #Read (Đọc):
    print("Đọc phần tử tại vị trí 1:", stack.read(1))
    #Update (Cập nhật):
    print("Cập nhật phần tử tại vị trí 1 thành 10:", stack.update(1, 10))
    print("Stack sau khi cập nhật:", stack)
    #Delete (Xóa):
    print("Xóa phần tử tại vị trí 1:", stack.delete(1))
    print("Stack sau khi xóa:", stack)

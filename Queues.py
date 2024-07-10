class Queue:
    def __init__(self):
        """
        Khởi tạo một hàng đợi rỗng sử dụng danh sách.
        """
        self.items = []

    def is_empty(self):
        """
        Kiểm tra xem hàng đợi có rỗng hay không.
        Trả về True nếu rỗng, ngược lại trả về False.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Thêm một phần tử vào cuối hàng đợi.

        Parameters:
        item (Any): Phần tử cần thêm vào hàng đợi.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Loại bỏ và trả về phần tử đầu tiên trong hàng đợi.

        Returns:
        Any: Phần tử đầu tiên trong hàng đợi.

        Raises:
        IndexError: Nếu hàng đợi rỗng.
        """
        if self.is_empty():
            raise IndexError("dequeue từ hàng đợi rỗng")
        return self.items.pop(0)

    def peek(self):
        """
        Trả về phần tử đầu tiên trong hàng đợi mà không loại bỏ nó.

        Returns:
        Any: Phần tử đầu tiên trong hàng đợi.

        Raises:
        IndexError: Nếu hàng đợi rỗng.
        """
        if self.is_empty():
            raise IndexError("peek từ hàng đợi rỗng")
        return self.items[0]

    def size(self):
        """
        Trả về số lượng phần tử hiện có trong hàng đợi.

        Returns:
        int: Số lượng phần tử trong hàng đợi.
        """
        return len(self.items)

    def get_all(self):
        """
        Trả về danh sách tất cả các phần tử trong hàng đợi.

        Returns:
        list: Danh sách các phần tử trong hàng đợi.
        """
        return self.items.copy()

    def update(self, index, item):
        """
        Cập nhật phần tử ở vị trí cụ thể trong hàng đợi.

        Parameters:
        index (int): Vị trí của phần tử cần cập nhật.
        item (Any): Giá trị mới cho phần tử.

        Raises:
        IndexError: Nếu chỉ số nằm ngoài phạm vi của danh sách.
        """
        if index < 0 or index >= len(self.items):
            raise IndexError("chỉ số nằm ngoài phạm vi của danh sách")
        self.items[index] = item

    def search(self, item):
        """
        Tìm kiếm phần tử trong hàng đợi và trả về vị trí của nó.

        Parameters:
        item (Any): Phần tử cần tìm kiếm.

        Returns:
        int: Vị trí của phần tử trong hàng đợi, hoặc -1 nếu không tìm thấy.
        """
        for index, current_item in enumerate(self.items):
            if current_item == item:
                return index
        return -1

    def __str__(self):
        """
        Trả về chuỗi biểu diễn của hàng đợi.

        Returns:
        str: Chuỗi biểu diễn của hàng đợi.
        """
        return "Queue: " + str(self.items)


# Sử dụng lớp Queue
queue = Queue()
print(queue)  # Queue: []

# Thêm phần tử vào hàng đợi
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # Queue: [1, 2, 3]

# Kiểm tra phần tử đầu tiên mà không loại bỏ
print(queue.peek())  # 1

# Loại bỏ phần tử đầu tiên trong hàng đợi
print(queue.dequeue())  # 1
print(queue)  # Queue: [2, 3]

# Kiểm tra kích thước hàng đợi
print(queue.size())  # 2

# Kiểm tra hàng đợi có rỗng hay không
print(queue.is_empty())  # False

# Lấy tất cả các phần tử trong hàng đợi
print(queue.get_all())  # [2, 3]

# Cập nhật phần tử ở vị trí thứ 1
queue.update(1, 4)
print(queue)  # Queue: [2, 4]

# Tìm kiếm phần tử trong hàng đợi
print(queue.search(2))  # 0
print(queue.search(4))  # 1
print(queue.search(5))  # -1

# Loại bỏ tất cả các phần tử
print(queue.dequeue())  # 2
print(queue.dequeue())  # 4

# Kiểm tra hàng đợi có rỗng hay không
print(queue.is_empty())  # True

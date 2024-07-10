class Node:
    """
    Lớp Node đại diện cho mỗi phần tử trong danh sách liên kết đôi.
    Chứa dữ liệu và con trỏ tới nút tiếp theo và nút trước đó.
    """

    class Node:
        """
        Lớp Node đại diện cho mỗi phần tử trong danh sách liên kết đôi.
        Chứa dữ liệu và con trỏ tới nút tiếp theo và nút trước đó.
        """

        def __init__(self, data):
            self.data = data  # Khởi tạo dữ liệu của nút
            self.next = None  # Khởi tạo con trỏ tới nút tiếp theo là None
            self.prev = None  # Khởi tạo con trỏ tới nút trước đó là None

    class DoublyLinkedList:
        """
        Lớp DoublyLinkedList cung cấp các phương thức để thao tác với danh sách liên kết đôi.
        """

        def __init__(self):
            self.head = None  # Khởi tạo đầu của danh sách là None

        def append(self, data):
            """
            Thêm một nút mới vào cuối danh sách.
            """
            new_node = Node(data)  # Tạo một nút mới với dữ liệu được cung cấp
            if not self.head:  # Nếu danh sách trống, đặt nút mới là đầu của danh sách
                self.head = new_node
                return
            last = self.head  # Bắt đầu từ đầu danh sách
            while last.next:  # Duyệt đến nút cuối cùng
                last = last.next
            last.next = new_node  # Liên kết nút cuối cùng với nút mới
            new_node.prev = last  # Liên kết nút mới với nút cuối cùng

        def prepend(self, data):
            """
            Thêm một nút mới vào đầu danh sách.
            """
            new_node = Node(data)  # Tạo một nút mới với dữ liệu được cung cấp
            if not self.head:  # Nếu danh sách trống, đặt nút mới là đầu của danh sách
                self.head = new_node
                return
            self.head.prev = new_node  # Liên kết đầu hiện tại với nút mới
            new_node.next = self.head  # Liên kết nút mới với đầu hiện tại
            self.head = new_node  # Cập nhật đầu của danh sách là nút mới

        def delete(self, node):
            """
            Xóa một nút khỏi danh sách.
            """
            if self.head is None or node is None:  # Nếu danh sách trống hoặc nút cần xóa là None, không làm gì cả
                return
            if self.head == node:  # Nếu nút cần xóa là đầu danh sách, cập nhật đầu danh sách
                self.head = node.next
            if node.next:  # Nếu nút cần xóa không phải là nút cuối
                node.next.prev = node.prev
            if node.prev:  # Nếu nút cần xóa không phải là nút đầu tiên
                node.prev.next = node.next
            node.next = node.prev = None  # Ngắt liên kết của nút cần xóa

        def display(self):
            """
            Hiển thị nội dung của danh sách.
            """
            elems = []
            current = self.head  # Bắt đầu từ đầu danh sách
            while current:  # Duyệt qua danh sách và thêm dữ liệu của từng nút vào danh sách elems
                elems.append(current.data)
                current = current.next
            print("Danh sách liên kết đôi:", elems)

        def update(self, old_data, new_data):
            """
            Cập nhật dữ liệu của nút có giá trị old_data thành new_data.
            """
            current = self.head
            while current:  # Duyệt qua danh sách để tìm nút có dữ liệu cần cập nhật
                if current.data == old_data:
                    current.data = new_data  # Cập nhật dữ liệu
                    return True
                current = current.next
            return False  # Trả về False nếu không tìm thấy nút cần cập nhật

        def find(self, data):
            """
            Tìm một nút trong danh sách theo giá trị dữ liệu và trả về nút đó.
            """
            current = self.head
            while current:  # Duyệt qua danh sách để tìm nút có dữ liệu cần tìm
                if current.data == data:
                    return current  # Trả về nút nếu tìm thấy
                current = current.next
            return None  # Trả về None nếu không tìm thấy

    # Ví dụ sử dụng:
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.display()

    # Cập nhật giá trị của nút có dữ liệu là 2 thành 20
    dll.update(2, 20)
    dll.display()

    # Tìm và xóa nút có dữ liệu là 20
    node_to_delete = dll.find(20)
    dll.delete(node_to_delete)
    dll.display()


class DoublyLinkedList:
    """
    Lớp DoublyLinkedList cung cấp các phương thức để thao tác với danh sách liên kết đôi.
    """

    def __init__(self):
        self.head = None  # Khởi tạo đầu của danh sách là None

    def append(self, data):
        """
        Thêm một nút mới vào cuối danh sách.
        """
        new_node = Node(data)  # Tạo một nút mới với dữ liệu được cung cấp
        if not self.head:  # Nếu danh sách trống, đặt nút mới là đầu của danh sách
            self.head = new_node
            return
        last = self.head  # Bắt đầu từ đầu danh sách
        while last.next:  # Duyệt đến nút cuối cùng
            last = last.next
        last.next = new_node  # Liên kết nút cuối cùng với nút mới
        new_node.prev = last  # Liên kết nút mới với nút cuối cùng

    def prepend(self, data):
        """
        Thêm một nút mới vào đầu danh sách.
        """
        new_node = Node(data)  # Tạo một nút mới với dữ liệu được cung cấp
        if not self.head:  # Nếu danh sách trống, đặt nút mới là đầu của danh sách
            self.head = new_node
            return
        self.head.prev = new_node  # Liên kết đầu hiện tại với nút mới
        new_node.next = self.head  # Liên kết nút mới với đầu hiện tại
        self.head = new_node  # Cập nhật đầu của danh sách là nút mới

    def delete(self, node):
        """
        Xóa một nút khỏi danh sách.
        """
        if self.head is None or node is None:  # Nếu danh sách trống hoặc nút cần xóa là None, không làm gì cả
            return
        if self.head == node:  # Nếu nút cần xóa là đầu danh sách, cập nhật đầu danh sách
            self.head = node.next
        if node.next:  # Nếu nút cần xóa không phải là nút cuối
            node.next.prev = node.prev
        if node.prev:  # Nếu nút cần xóa không phải là nút đầu tiên
            node.prev.next = node.next
        node.next = node.prev = None  # Ngắt liên kết của nút cần xóa

    def display(self):
        """
        Hiển thị nội dung của danh sách.
        """
        elems = []
        current = self.head  # Bắt đầu từ đầu danh sách
        while current:  # Duyệt qua danh sách và thêm dữ liệu của từng nút vào danh sách elems
            elems.append(current.data)
            current = current.next
        print("Danh sách liên kết đôi:", elems)

    def update(self, old_data, new_data):
        """
        Cập nhật dữ liệu của nút có giá trị old_data thành new_data.
        """
        current = self.head
        while current:  # Duyệt qua danh sách để tìm nút có dữ liệu cần cập nhật
            if current.data == old_data:
                current.data = new_data  # Cập nhật dữ liệu
                return True
            current = current.next
        return False  # Trả về False nếu không tìm thấy nút cần cập nhật

    def find(self, data):
        """
        Tìm một nút trong danh sách theo giá trị dữ liệu và trả về nút đó.
        """
        current = self.head
        while current:  # Duyệt qua danh sách để tìm nút có dữ liệu cần tìm
            if current.data == data:
                return current  # Trả về nút nếu tìm thấy
            current = current.next
        return None  # Trả về None nếu không tìm thấy


# Ví dụ sử dụng:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display()

# Cập nhật giá trị của nút có dữ liệu là 2 thành 20
dll.update(2, 20)
dll.display()

# Tìm và xóa nút có dữ liệu là 20
node_to_delete = dll.find(20)
dll.delete(node_to_delete)
dll.display()

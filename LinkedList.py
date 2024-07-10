class Node:
    """
    Một nút trong danh sách liên kết đơn.

    Thuộc tính:
    -----------
    data : bất kỳ kiểu dữ liệu nào
        Dữ liệu được lưu trữ trong nút.
    next_node : Node
        Tham chiếu đến nút tiếp theo trong danh sách.
    """

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """
    Danh sách liên kết đơn.

    Thuộc tính:
    -----------
    head : Node
        Nút đầu tiên của danh sách liên kết.

    Phương thức:
    -----------
    append(data):
        Thêm một nút với dữ liệu cho trước vào cuối danh sách.
    prepend(data):
        Thêm một nút với dữ liệu cho trước vào đầu danh sách.
    delete_with_value(data):
        Xóa nút đầu tiên với dữ liệu cho trước.
    print_list():
        In ra dữ liệu của tất cả các nút trong danh sách.
    search(data):
        Tìm kiếm và trả về nút đầu tiên chứa dữ liệu cho trước.
    update(old_data, new_data):
        Cập nhật dữ liệu của nút đầu tiên chứa dữ liệu cũ cho thành dữ liệu mới.
    """

    def __init__(self):
        """
        Khởi tạo danh sách liên kết với head là None.
        """
        self.head = None

    def append(self, data):
        """
        Thêm một nút với dữ liệu cho trước vào cuối danh sách.

        Parameters:
        -----------
        data : bất kỳ kiểu dữ liệu nào
            Dữ liệu của nút mới.

        Returns:
        --------
        None
        """
        if not self.head:
            # Nếu danh sách trống, gán nút đầu tiên
            self.head = Node(data)
            return
        current_node = self.head
        # Duyệt đến nút cuối cùng
        while current_node.next_node:
            current_node = current_node.next_node
        # Thêm nút mới vào cuối danh sách
        current_node.next_node = Node(data)

    def prepend(self, data):
        """
        Thêm một nút với dữ liệu cho trước vào đầu danh sách.

        Parameters:
        -----------
        data : bất kỳ kiểu dữ liệu nào
            Dữ liệu của nút mới.

        Returns:
        --------
        None
        """
        new_head = Node(data)
        new_head.next_node = self.head
        self.head = new_head

    def delete_with_value(self, data):
        """
        Xóa nút đầu tiên với dữ liệu cho trước.

        Parameters:
        -----------
        data : bất kỳ kiểu dữ liệu nào
            Dữ liệu của nút cần xóa.

        Returns:
        --------
        None
        """
        if not self.head:
            # Nếu danh sách trống, không làm gì cả
            return
        if self.head.data == data:
            # Nếu nút đầu tiên có dữ liệu cần xóa
            self.head = self.head.next_node
            return
        current_node = self.head
        # Duyệt qua các nút để tìm nút có dữ liệu cần xóa
        while current_node.next_node:
            if current_node.next_node.data == data:
                # Bỏ qua nút có dữ liệu cần xóa
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node

    def print_list(self):
        """
        In ra dữ liệu của tất cả các nút trong danh sách.

        Returns:
        --------
        None
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def search(self, data):
        """
        Tìm kiếm và trả về nút đầu tiên chứa dữ liệu cho trước.

        Parameters:
        -----------
        data : bất kỳ kiểu dữ liệu nào
            Dữ liệu cần tìm.

        Returns:
        --------
        Node hoặc None
            Trả về nút chứa dữ liệu nếu tìm thấy, None nếu không tìm thấy.
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next_node
        return None

    def update(self, old_data, new_data):
        """
        Cập nhật dữ liệu của nút đầu tiên chứa dữ liệu cũ cho thành dữ liệu mới.

        Parameters:
        -----------
        old_data : bất kỳ kiểu dữ liệu nào
            Dữ liệu cần cập nhật.
        new_data : bất kỳ kiểu dữ liệu nào
            Dữ liệu mới thay thế.

        Returns:
        --------
        None
        """
        node_to_update = self.search(old_data)
        if node_to_update:
            node_to_update.data = new_data


# Ví dụ sử dụng:
if __name__ == "__main__":
    ll = LinkedList()
    # Thêm
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    # In
    print("Danh sách ban đầu:")
    ll.print_list()
    # Xoá
    print("\nSau khi xóa nút có giá trị 2:")
    ll.delete_with_value(2)
    ll.print_list()
    # Cập nhật
    print("\nCập nhật nút có giá trị 1 thành 10:")
    ll.update(1, 10)
    ll.print_list()
    # Tìm kiếm
    print("\nTìm kiếm nút có giá trị 3:")
    node = ll.search(3)
    if node:
        print(f"Đã tìm thấy nút với giá trị: {node.data}")
    else:
        print("Không tìm thấy nút với giá trị này.")

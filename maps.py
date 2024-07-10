class MapBase:
    """Lớp cơ sở cho các bản đồ."""

    class _Item:
        """Lớp con để lưu trữ các cặp key-value."""

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __str__(self):
            return f'({self._key}, {self._value})'


class UnsortedMap(MapBase):
    """Lớp Map sử dụng danh sách chưa được sắp xếp."""

    def __init__(self):
        """Khởi tạo một bản đồ trống."""
        self._table = []

    def create(self, key, value):
        """Thêm một cặp key-value mới vào bản đồ.
        Nếu key đã tồn tại, cập nhật giá trị của nó."""
        for item in self._table:
            if key == item._key:
                item._value = value  # Update (Cập nhật)
                return
        self._table.append(self._Item(key, value))  # Create (Tạo mới)

    def read(self, key):
        """Đọc giá trị liên kết với key (key).
        Trả về giá trị nếu tìm thấy, nếu không, ném ra ngoại lệ KeyError."""
        for item in self._table:
            if key == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(key))

    def update(self, key, value):
        """Cập nhật giá trị liên kết với key (key).
        Nếu key không tồn tại, ném ra ngoại lệ KeyError."""
        for item in self._table:
            if key == item._key:
                item._value = value  # Update (Cập nhật)
                return
        raise KeyError('Key Error: ' + repr(key))

    def delete(self, key):
        """Xóa mục có key khỏi bản đồ.
        Nếu key không tồn tại, ném ra ngoại lệ KeyError."""
        for j in range(len(self._table)):
            if key == self._table[j]._key:
                self._table.pop(j)  # Delete (Xóa)
                return
        raise KeyError('Key Error: ' + repr(key))

    def search(self, value):
        """Tìm kiếm các key có giá trị tương ứng với value.
        Trả về danh sách các key tìm thấy."""
        result = []
        for item in self._table:
            if item._value == value:
                result.append(item._key)
        return result

    def __len__(self):
        """Trả về số lượng mục trong bản đồ."""
        return len(self._table)

    def __iter__(self):
        """Tạo một iterator cho các key của bản đồ."""
        for item in self._table:
            yield item._key


# Ví dụ sử dụng lớp UnsortedMap
if __name__ == "__main__":
    m = UnsortedMap()

    # Create (Tạo mới)
    m.create("a", 1)
    m.create("b", 2)
    m.create("c", 3)
    m.create("d", 2)

    # Read (Đọc)
    print("Giá trị của key 'a':", m.read("a"))  # Kết quả: 1

    # Update (Cập nhật)
    m.update("a", 10)
    print("Giá trị mới của key 'a':", m.read("a"))  # Kết quả: 10

    # Xóa (Delete)
    m.delete("b")
    try:
        print("Giá trị của key 'b':", m.read("b"))  # KeyError: Key Error: 'b'
    except KeyError as e:
        print(e)

    # Tìm kiếm các key với giá trị 2
    keys_with_value_2 = m.search(2)
    print("Các key có giá trị là 2:", keys_with_value_2)  # Kết quả: ['d']

    # Đếm số lượng mục
    print("Số lượng mục trong bản đồ:", len(m))  # Kết quả: 2

    # Duyệt qua các key
    for key in m:
        print(f'{key}: {m.read(key)}')

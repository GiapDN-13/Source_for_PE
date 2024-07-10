class CustomSet:
    def __init__(self, elements=None):
        """
        Hàm khởi tạo của lớp CustomSet.
        elements: là một danh sách các phần tử để khởi tạo tập hợp.
        """
        # Sử dụng set để lưu trữ các phần tử và đảm bảo các phần tử là duy nhất
        self.elements = set(elements) if elements else set()

    def create(self, element):
        """
        Thêm một phần tử vào tập hợp.
        element: phần tử cần thêm vào tập hợp.
        """
        self.elements.add(element)
        print(f"Phần tử '{element}' đã được thêm vào tập hợp.")

    def read(self):
        """
        Trả về tập hợp các phần tử hiện tại.
        """
        return self.elements

    def update(self, old_element, new_element):
        """
        Cập nhật một phần tử trong tập hợp.
        old_element: phần tử cần thay thế.
        new_element: phần tử mới thay thế.
        """
        if old_element in self.elements:
            self.elements.remove(old_element)
            self.elements.add(new_element)
            print(f"Phần tử '{old_element}' đã được thay thế bằng '{new_element}'.")
        else:
            print(f"Phần tử '{old_element}' không tồn tại trong tập hợp.")

    def delete(self, element):
        """
        Xóa một phần tử khỏi tập hợp.
        element: phần tử cần xóa.
        """
        if element in self.elements:
            self.elements.remove(element)
            print(f"Phần tử '{element}' đã được xóa khỏi tập hợp.")
        else:
            print(f"Phần tử '{element}' không tồn tại trong tập hợp.")

    def contains(self, element):
        """
        Kiểm tra xem một phần tử có nằm trong tập hợp hay không.
        element: phần tử cần kiểm tra.
        """
        return element in self.elements

    def union(self, other_set):
        """
        Trả về một tập hợp mới là hợp của tập hợp hiện tại và tập hợp khác.
        other_set: tập hợp khác.
        """
        return CustomSet(self.elements.union(other_set.elements))

    def intersection(self, other_set):
        """
        Trả về một tập hợp mới là giao của tập hợp hiện tại và tập hợp khác.
        other_set: tập hợp khác.
        """
        return CustomSet(self.elements.intersection(other_set.elements))

    def difference(self, other_set):
        """
        Trả về một tập hợp mới là hiệu của tập hợp hiện tại và tập hợp khác.
        other_set: tập hợp khác.
        """
        return CustomSet(self.elements.difference(other_set.elements))

    def is_subset(self, other_set):
        """
        Kiểm tra xem tập hợp hiện tại có phải là tập hợp con của tập hợp khác không.
        other_set: tập hợp khác.
        """
        return self.elements.issubset(other_set.elements)

    def is_superset(self, other_set):
        """
        Kiểm tra xem tập hợp hiện tại có phải là tập hợp cha của tập hợp khác không.
        other_set: tập hợp khác.
        """
        return self.elements.issuperset(other_set.elements)

    def __str__(self):
        """
        Trả về chuỗi biểu diễn của tập hợp.
        """
        return f"CustomSet({self.elements})"

# Ví dụ sử dụng
if __name__ == "__main__":
    # Khởi tạo tập hợp
    custom_set = CustomSet([1, 2, 3])
    print(custom_set)  # Output: CustomSet({1, 2, 3})

    # Thêm phần tử
    custom_set.create(4)
    print(custom_set)  # Output: CustomSet({1, 2, 3, 4})

    # Đọc tập hợp
    print("Tập hợp hiện tại:", custom_set.read())  # Output: Tập hợp hiện tại: {1, 2, 3, 4}

    # Cập nhật phần tử
    custom_set.update(4, 5)
    print(custom_set)  # Output: CustomSet({1, 2, 3, 5})

    # Xóa phần tử
    custom_set.delete(5)
    print(custom_set)  # Output: CustomSet({1, 2, 3})

    # Kiểm tra phần tử
    print("Tập hợp chứa 2:", custom_set.contains(2))  # Output: Tập hợp chứa 2: True
    print("Tập hợp chứa 5:", custom_set.contains(5))  # Output: Tập hợp chứa 5: False

    # Hợp của hai tập hợp
    another_set = CustomSet([3, 4, 5])
    union_set = custom_set.union(another_set)
    print("Hợp:", union_set)  # Output: Hợp: CustomSet({1, 2, 3, 4, 5})

    # Giao của hai tập hợp
    intersection_set = custom_set.intersection(another_set)
    print("Giao:", intersection_set)  # Output: Giao: CustomSet({3})

    # Hiệu của hai tập hợp
    difference_set = custom_set.difference(another_set)
    print("Hiệu:", difference_set)  # Output: Hiệu: CustomSet({1, 2})

    # Kiểm tra tập hợp con
    print("custom_set là tập hợp con của another_set:", custom_set.is_subset(another_set))  # Output: custom_set là tập hợp con của another_set: False

    # Kiểm tra tập hợp cha
    print("custom_set là tập hợp cha của another_set:", custom_set.is_superset(another_set))  # Output: custom_set là tập hợp cha của another_set: False

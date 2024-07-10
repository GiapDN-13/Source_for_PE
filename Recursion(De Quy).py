class Factorial:
    def __init__(self, number):
        """
        Khởi tạo đối tượng Factorial với một số nguyên không âm.

        :param number: Số nguyên không âm cần tính giai thừa.
        """
        if number < 0:
            raise ValueError("Number must be non-negative")
        self.number = number

    def calculate(self):
        """
        Phương thức tính giai thừa sử dụng đệ quy.

        :return: Giai thừa của số nguyên đã cho.
        """
        return self._recursive_factorial(self.number)

    def _recursive_factorial(self, n):
        """
        Phương thức đệ quy riêng để tính giai thừa của một số nguyên.

        :param n: Số nguyên hiện tại trong quá trình tính toán đệ quy.
        :return: Giai thừa của số nguyên n.
        """
        if n == 0:
            return 1
        else:
            return n * self._recursive_factorial(n - 1)


class FactorialManager:
    def __init__(self):
        """
        Khởi tạo đối tượng FactorialManager để quản lý các đối tượng Factorial.
        """
        self.factorials = []

    def create_factorial(self, number):
        """
        Tạo và thêm một đối tượng Factorial mới vào danh sách.

        :param number: Số nguyên không âm cần tính giai thừa.
        :return: Đối tượng Factorial đã được tạo.
        """
        factorial = Factorial(number)
        self.factorials.append(factorial)
        return factorial

    def read_factorial(self, index):
        """
        Đọc và trả về đối tượng Factorial tại vị trí chỉ định.

        :param index: Vị trí của đối tượng Factorial trong danh sách.
        :return: Đối tượng Factorial tại vị trí chỉ định.
        """
        if 0 <= index < len(self.factorials):
            return self.factorials[index]
        else:
            raise IndexError("Index out of range")

    def update_factorial(self, index, new_number):
        """
        Cập nhật số nguyên không âm của đối tượng Factorial tại vị trí chỉ định.

        :param index: Vị trí của đối tượng Factorial trong danh sách.
        :param new_number: Số nguyên không âm mới cần tính giai thừa.
        :return: Đối tượng Factorial đã được cập nhật.
        """
        if 0 <= index < len(self.factorials):
            self.factorials[index] = Factorial(new_number)
            return self.factorials[index]
        else:
            raise IndexError("Index out of range")

    def delete_factorial(self, index):
        """
        Xóa đối tượng Factorial tại vị trí chỉ định khỏi danh sách.

        :param index: Vị trí của đối tượng Factorial trong danh sách.
        """
        if 0 <= index < len(self.factorials):
            del self.factorials[index]
        else:
            raise IndexError("Index out of range")


# Ví dụ sử dụng các chức năng CRUD:
if __name__ == "__main__":
    manager = FactorialManager()

    # Create: Tạo các đối tượng Factorial
    f1 = manager.create_factorial(5)
    f2 = manager.create_factorial(7)

    # Read: Đọc và in giai thừa của các đối tượng Factorial
    print(f"Giai thừa của {f1.number} là {f1.calculate()}")
    print(f"Giai thừa của {f2.number} là {f2.calculate()}")

    # Update: Cập nhật số của đối tượng Factorial
    updated_factorial = manager.update_factorial(0, 10)
    print(f"Giai thừa của {updated_factorial.number} là {updated_factorial.calculate()}")

    # Delete: Xóa một đối tượng Factorial
    manager.delete_factorial(1)
    # Kiểm tra danh sách sau khi xóa
    for i, factorial in enumerate(manager.factorials):
        print(f"Index {i}: Giai thừa của {factorial.number} là {factorial.calculate()}")

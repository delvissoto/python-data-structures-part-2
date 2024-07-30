class Array:
    def __init__(self, size=10):
        self.size = size
        self.array = [None] * size
        self.current_size = 0

    def add_element(self, element):
        if self.current_size == self.size:
            self._resize()
        self.array[self.current_size] = element
        self.current_size += 1

    def get_element(self, index):
        if 0 <= index < self.current_size:
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def remove_element(self, index):
        if 0 <= index < self.current_size:
            for i in range(index, self.current_size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.current_size - 1] = None
            self.current_size -= 1
        else:
            raise IndexError("Index out of range")

    def print_array(self):
        print(self.array[:self.current_size])

    def _resize(self):
        self.size *= 2
        new_array = [None] * self.size
        for i in range(self.current_size):
            new_array[i] = self.array[i]
        self.array = new_array

# Test cases
my_array = Array()

# Adding elements
my_array.add_element(1)
my_array.add_element(2)
my_array.add_element(3)

# Printing the array
print("Original Array:")
my_array.print_array()

# Getting element at index
print("\nElement at index 1:", my_array.get_element(1))

# Removing element at index
my_array.remove_element(1)
print("\nArray after removing element at index 1:")
my_array.print_array()

# Trying to remove element at an invalid index
try:
    my_array.remove_element(5)
except IndexError as e:
    print("\n", e)
import random

class Arrays():
    @staticmethod
    def create_array_with_same_values(number_of_array_elements, value_of_array_elements):
        array = []
        for i in range(number_of_array_elements):
            array.append(value_of_array_elements)
        return array
    @staticmethod
    def create_array_with_random_values(number_of_array_elements, value_from, value_to):
        array = []
        for j in range(number_of_array_elements):
            array.append(random.randint(value_from, value_to))
        return array
    @staticmethod
    def count_values_in_range(array, value_from, value_to):
        count = 0
        for element in array:
            if element >= value_from and element <= value_to:
                count += 1
        return count


array1=Arrays.create_array_with_same_values(10,5)
print(array1)
array2=Arrays.create_array_with_random_values(10,2,5)
print(array2)
array3=[4,5,6]
count1=Arrays.count_values_in_range(array3,4,5)
print(array3)

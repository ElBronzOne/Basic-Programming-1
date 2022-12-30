import random

class Array:
    def create_array_with_random_values(number_of_array_elements, value_from, value_to):
        array = []
        for i in range(number_of_array_elements):
            array.append(random.randint(value_from, value_to))
        return array

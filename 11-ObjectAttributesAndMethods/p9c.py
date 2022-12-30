class Array:
    def count_values_in_range(array, value_from, value_to):
        count = 0
        for element in array:
            if value_from <= element <= value_to:
                count += 1
        return count

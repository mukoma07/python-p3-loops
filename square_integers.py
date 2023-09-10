def square_integers(numbers):
    squared_list = []  # Create an empty list to store squared elements
    
    for num in numbers:
        if isinstance(num, int):  # Check if the element is an integer
            squared_list.append(num ** 2)  # Square the integer and append to the list
    
    return squared_list

# Example usage:
input_list = [1, 2, 3, 4, 5]
result = square_integers(input_list)
print(result)  # Output will be [1, 4, 9, 16, 25]

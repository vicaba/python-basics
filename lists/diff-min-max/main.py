def find_difference(numbers):
    # Check if the list is empty
    if not numbers:
        return "La lista está vacía"

    # Find the maximum and minimum numbers
    max_number = max(numbers)
    min_number = min(numbers)

    # Calculate the difference
    difference = max_number - min_number

    return difference

def main():
    numbers = [5, 10, 15, 20, 25]
    print(find_difference(numbers))

    # Test the function with an empty list
    empty_list = []
    print(find_difference(empty_list))

if __name__ == "__main__":
    main()
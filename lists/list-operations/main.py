def main():
    # Create a list with numbers from 1 to 10
    numbers = list(range(1, 11))

    # Print all elements of the list
    print("All elements of the list:")
    print(numbers)

    # Print the third element of the list
    print("The third element of the list:")
    print(numbers[2])

    # Print the last three elements of the list
    print("The last three elements of the list:")
    print(numbers[-3:])

    # Append the number 11 to the end of the list and then print it
    numbers.append(11)
    print("List after appending the number 11:")
    print(numbers)

    # Remove the first element from the list
    del numbers[0]
    print("List after removing the first element:")
    print(numbers)

    # Replace the second element of the list with the number 20
    numbers[1] = 20
    print("List after replacing the second element with the number 20:")
    print(numbers)

    # Check if the number 5 is in the list and print an appropriate message
    if 5 in numbers:
        print("The number 5 is in the list.")
    else:
        print("The number 5 is not in the list.")

    # Print the length of the list
    print("The length of the list is:")
    print(len(numbers))

if __name__ == "__main__":
    main()
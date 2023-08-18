def main():
    # Create a dictionary representing a phone book
    phone_book = {'Peter': '123-4567', 'Anna': '987-6543', 'Luis': '789-0123'}

    # Print the entire dictionary
    print("Entire phone book:")
    print(phone_book)

    # Print only the names of the people in the phone book
    print("Names in the phone book:")
    print(phone_book.keys())

    # Print only the phone numbers
    print("Phone numbers in the phone book:")
    print(phone_book.values())

    # Add another person to the phone book with their phone number
    phone_book['Maria'] = '456-7890'
    print("Phone book after adding Maria:")
    print(phone_book)

    # Remove a person from the phone book
    del phone_book['Peter']
    print("Phone book after removing Peter:")
    print(phone_book)

    # Change a person's phone number
    phone_book['Anna'] = '111-2222'
    print("Phone book after changing Anna's number:")
    print(phone_book)

    # Check if a person is in the phone book and print an appropriate message
    if 'Luis' in phone_book:
        print("Luis is in the phone book.")
    else:
        print("Luis is not in the phone book.")

    # Print the number of contacts in the phone book
    print("The number of contacts in the phone book is:")
    print(len(phone_book))

if __name__ == "__main__":
    main()
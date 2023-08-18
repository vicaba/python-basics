# Function to determine if a number is prime
def is_prime(n):
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
    return True

def main():
    # Create a list with several numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Create a new list with only the even numbers from the original list
    evens = [num for num in numbers if num % 2 == 0]
    print("Even numbers:")
    print(evens)

    # Create a new list with the square of each number from the original list
    squares = [num ** 2 for num in numbers]
    print("Squares of the numbers:")
    print(squares)

    # Create a new list with only the numbers that are at an odd index position
    odd_indices = [num for i, num in enumerate(numbers) if i % 2 != 0]
    print("Numbers at odd index positions:")
    print(odd_indices)

    # Create a new list with only the numbers that are prime
    primes = [num for num in numbers if is_prime(num)]
    print("Prime numbers:")
    print(primes)


if __name__ == "__main__":
    main()
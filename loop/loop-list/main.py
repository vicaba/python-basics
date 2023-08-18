# Part 1
def p1(numbers):
    for number in numbers:
        print(number)

# Part 2
def p2(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

    # Part 3

def p3(numbers):
    for number in numbers:
        print(number ** 2)

if __name__ == "__main__":
    numbers = [12, 45, 2, 10, 78, 5, 15, 56, 8, 32, 89, 52]
    p1(numbers)
    p2(numbers)
    p3(numbers)
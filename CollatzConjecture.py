# Start with a number n > 1. Find the number of steps it takes to reach one using the following process
# If n is even divide it by 2. If n is odd, multiply it by 3 and add 1.

number = int(input("Please input a number n > 1: "))
counter = 0

while number != 1:
    if (number % 2) == 0:
        number /= 2
        counter += 1
    else:
        number = number * 3 + 1
        counter += 1

print(counter)
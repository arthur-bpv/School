import math

numbers = []
def menu():
    print('INFOR2 SYSTEM\n1 - Read a number\n2 - Max and Min\n3 - List\n4 - Second largest\n5 - Prime Number Identifier\n6 - Binary\n7 - Quit\n')

def readnumber():
    x = int(input('Write: '))
    numbers.append(x)
    print(f'Number {x} added successfully\n')

    again = input('Do you want to add another number? ')
    if again == 'y':
        readnumber()
def maxmin():
    if numbers:
        print(f'Max: {max(numbers)}\nMin: {min(numbers)}\n')
    else:
        print('Empty list\n')

def Print():
    if numbers:
        for i in numbers:
            print(i, end=' ')
        print()
    else:
        print('Empty list\n')


def second_largest():
    second = 0
    for i in numbers:
        if i < max(numbers) and i > second:
            second = i
    print(f'The second largest number is {second}\n')


def prime_identifier():
    if numbers:
        primes = []
        for i in numbers:
            prime = True
            for j in range(2, int(math.sqrt(i) + 1)):
                if i % j == 0:
                    prime = False
                    break
            if prime and i > 1:
                primes.append(i)

        if primes:
            print(f'Prime numbers are: {primes}')
        else:
            print(f'No prime numbers found')
    else:
        print('List is empty\n')


def binary():
    bin_list = []
    if numbers:
        for i in numbers:
            binary = ''
            quotient = i
            while quotient > 0:
                adc = quotient % 2
                quotient = quotient // 2
                binary += str(adc)

            binary = binary[::-1]
            bin_list.append(binary)
        print(f'The binary: {bin_list}\n')


    else:
        print('List is empty\n')


while True:
    menu()
    op = int(input('Choose an option: '))
    if op == 1:
        readnumber()
    elif op == 2:
        maxmin()
    elif op == 3:
        Print()
    elif op == 4:
        second_largest()
    elif op == 5:
        prime_identifier()
    elif op == 6:
        binary()
    elif op == 7:
        break
    else:
        print('INVALID')
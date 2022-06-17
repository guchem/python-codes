"""
name : getahun seyoum
id : ets0561/10
"""
import math


# 1
def qube(num):
    return num*num*num


# 2
def triangle(base, height):
    return base*height/2


# 3
def rectangle(base, height):
    return base*height


# 4
def line(m, b, x):
    return m*x + b


# 5
def intersect(m1, b1, m2, b2):
    if m1 == m2:
        if b1 == b2:
            return True
        return False
    x_intersection = (b2-b1)/(m1-m2)
    y_of_line1, y_of_line2 = x_intersection*m1+b1, x_intersection*m2+b2
    return y_of_line1 == y_of_line2


# 6
def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)


# 7
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    return fibonacci(num-2)+fibonacci(num-1)


# 8 a
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True


# 8 b
def sum_of_digits(num):
    sum_ = 0
    for i in str(num):
        sum_ += int(i)
    return sum_


# 9
def sort_numbers(*args):
    return sorted(args)


# 10
def mark_gt20():
    number_of_students = int(input("How many students do you have ? : "))
    marks_gt20 = 0
    for i in range(number_of_students):
        mark = int(input("please enter the mark of the next student out of 30 : "))
        while mark < 0 or mark>30:
            mark = int(input("the mark should be between 0 and 30 : "))
        if mark > 20:
            marks_gt20 += 1
    return marks_gt20


# 11
def phone():
    phone_no = input("Enter Your Number : ").strip()
    if len(phone_no) == 9 and phone_no.isdigit():
        if phone_no.startswith('9'):
            print('mobile')
        else:
            print('fixed phone')
    else:
        print('Invalid number')


# 12
def min_max():
    size = int(input("How many numbers do you have : "))
    numbers = []
    for i in range(size):
        numbers.append(int(input("Enter a number : ")))
    print(f'The maximum is {max(numbers)} and the minimum is {min(numbers)}')


# 13
def reverse():
    print(input("enter Your number : ")[::-1])


# for lcm and gcd
def factorize(number):
    factors = {}
    for i in range(number + 1):
        if is_prime(i):
            x = 0
            while number % i == 0:
                number = number / i
                x += 1
                if x > 0:
                    factors[i] = x
    return factors


# 14
def gcd(num1:int, num2:int):
    x_fact = factorize(num1)
    y_fact = factorize(num2)
    gcd = {}
    gcd_ = 1
    for key, value in x_fact.items():
        if y_fact.get(key):
            gcd[key] = value if value < y_fact.get(key) else y_fact.get(key)
    for key, value in gcd.items():
        gcd_ *= key ** value
    return gcd_


# 15
def lcm(num1:int,num2:int):
    x_fact = factorize(num1)
    y_fact = factorize(num2)
    lcm = {}
    lcm_ = 1
    for key,value in x_fact.items():
        lcm[key] = y_fact.get(key, -1) if y_fact.get(key, -1) > value else value
    for key,value in y_fact.items():
        if lcm.get(key, -1) == -1:
            lcm[key] = value
    for key,value in lcm.items():
        lcm_ *= int(key)**int(value)
    return lcm_


# 16
def series_sum():
    sum_ = 0
    for i in range(1, 98, 2):
        sum_ += i/(i+2)
    return sum_


# 17
def isbn():
    first_9 = input("Enter the first 9 digits : ")
    sum_ = 0
    for index, number in enumerate(first_9):
        sum_ += int(number) * (index+1)
    return first_9 + 'X' if sum_ % 11 == 10 else first_9 + str(sum_ % 11)


# 18
def e_to_x(power):
    result = 1
    for i in range(1, 990):
        result += (power**i)/factorial(i)
    return result


# 19
def leap_years():
    def is_leap(year):
        if year % 400 == 0:
            return True
        if year % 4==0:
            if year % 100 == 0:
                return False
            return True
        return False

    counter = 0
    for i in range(2001, 2101):
        if is_leap(i):
            counter += 1
            print(i, end=' ' if counter % 10 != 0 else '\n')


# 20
def occurrence(numbers):
    numbers = list(str(numbers))
    return f"the largest number is {(max(numbers))} and it has occurred {numbers.count(max(numbers))} times"


# 21
def to_be_qube():
    to_be_qubes = []
    for i in range(100, 1000):
        if i == int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3:
            to_be_qubes.append(i)
    return to_be_qubes


# 22
def int_length():
    while True:
        num = input("Enter Your number DO NOt USE COMMAS : ")

        if int(num) < 0:
            break

        print(f"{num} has {len(num)} digits")


# 23
def primes_between(num: int):
    primes = 0
    for i in range(2, num+1):
        if is_prime(i):
            primes += 1

    return primes


# 24
def is_perfect(num):
    divisors = []
    sum_ = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            divisors.append(i)
            sum_ += i
    if sum_ == num:
        # return True
        return f"{num} is a perfect number and its proper divisors are {divisors}"
    else:
        return False


# 25
def number_analysis():
    numbers = []

    def negative_positive():
        negatives = 0
        positives = 0
        for i in numbers:
            if i > 0:
                positives += 1
            else:
                negatives += 1
        return {'negatives': negatives, 'positives': positives}

    while True:
        input_ = int(input("Enter a number, Enter 0 if to Exit : "))
        if input_ == 0:
            print(f"Positive Numbers = {negative_positive()['positives']}")
            print(f"Negative Numbers = {negative_positive()['negatives']}")
            print(f'Total = {sum(numbers)}')
            print(f'Average = {sum(numbers)/len(numbers)}')
            break
        else:
            numbers.append(input_)


# 26
def tuition():
    initial = 10000
    rate = 0.05
    for i in range(10):
        initial += rate*initial
    print('after 10 years', initial)

    #  10th + 11th + 12th + 13th

    four_year_tuition = initial

    for i in range(3):
        four_year_tuition += initial + initial *rate

    return f"Four year tuition starting from 10 years from now = ${round(four_year_tuition,2)}"


# 27
def unit_converter():
    choice = input("Enter k for Kilogram to pound, m for mile-to-kilometer, h for hour-to-minute : ").lower().strip()
    value = input("Enter your value : ")
    if choice == 'k':
        return f'{value} Kilogram is equal to {float(value)*2.2046} Pounds'
    elif choice == 'm':
        return f'{value} miles is equal to {float(value)*1.609} kilometers'
    elif choice == 'h':
        return f'{value} hours is equal to {float(value.split(":")[0])*60 + float(value.split(":")[1]) if ":" in value else float(value)*60} minutes'

    else:
        return "Invalid Inputs"


# 28
def student_report():
    quantity = int(input("Enter number of students : "))
    marks = {}
    for i in range(quantity):
        name = input("Name of student : ")
        mark = float(input(f"Score of {name} : "))
        marks[name] = mark
    marks_sorted = sorted(marks.items(), key=lambda mark_: mark_[1], reverse=True)
    print(f"The highest scorer is {marks_sorted[0][0]} with {marks_sorted[0][1]} and The Second is {marks_sorted[1][0]} with {marks_sorted[1][1]}")


# 29
def student_report2():
    quantity = int(input("Enter number of students : "))
    marks = {}
    for i in range(quantity):
        name = input("Name of student : ")
        mark = float(input(f"Score of {name} : "))
        marks[name] = mark
    marks_sorted = sorted(marks.items(), key=lambda mark_: mark_[1], reverse=True)
    print(f"The highest scorer is {marks_sorted[0][0]} with {marks_sorted[0][1]}")


# 30
def nums_100_200():
    counter = 0
    for i in range(100, 201):
        if i % 5 == 0 and i % 6 != 0 or i % 6 == 0 and i % 5 != 0:
            counter += 1
            print(i, end='\n' if counter % 10 == 0 else ' ')


# 31
def ascii_chars():
    counter = 0
    for i in range(ord('!'), ord('~')+1):
        counter += 1
        print(chr(i), end='\n' if counter % 10 == 0 else ' ')


# 32 A
def pattern1():
    for i in range(1, 7):
        print(' '*(6-i), end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()


# 32 B
def pattern2():
    for i in range(1, 7):
        blanks = i-1
        print(' '*blanks, end='')
        for _ in range(1, 7-blanks):
            print(_, end='')
        print()


# 33
def pyramid():
    height = int(input("Enter the height of your pyramid : "))
    blanks = height - 1
    for i in range(1, height+1):
        print('  '*blanks, end='')
        for _ in range(i, 0, -1):
            if _ < 10:
                print(f" {_}", end='')
            else:
                print(_, end='')
        for _ in range(2, i+1):
            if _ < 10:
                print(f" {_}", end='')
            else:
                print(_, end='')
        print()
        blanks -= 1


# 34
def patter3():
    blanks = 7
    for i in range(blanks):
        print(' '*blanks, end='')
        for _ in range(i):
            print(2**_, end='')
        for _ in range(i-2, -1, -1):
            print(2**_, end='')
        blanks -= 1
        print()


# 35
def loan():
    # interest is per year

    amount = float(input('Loan amount : '))
    period = int(input('Period in years : '))
    base_rate = 0.05
    increment = 0.00125

    def interest(initial, interest_rate, duration):
        for i in range(duration):
            initial += initial*interest_rate
        return initial/(duration*12), initial

    print('Interest-Rate\tMonthly-Payment\tTotal-payment')
    while base_rate < 0.081:
        pay_per_month, total = interest(amount, base_rate, period)
        print(f'{round(base_rate*100,3)}%\t\t\t{round(pay_per_month,2)}\t\t\t{round(total,2)}')
        base_rate += increment


# 36
def dec_hex():
    number = int(input("Enter your Number : "))
    # return hex(number)
    remainders = []
    hexs = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number > 0:
        number, remainder = number // 16, number % 16
        remainders.append(str(hexs.get(remainder, remainder)))
    return '0x'+''.join(remainders[::-1])


# 37
def euler():
    e = 1
    for i in range(1, 100):
        e += 1/factorial(i)
    return e


# 38 same as # 8 a


# 39
def is_even(num):
    return num%2 == 0 if num>=2 else False


# 40
def calculator():
    expression = input("Enter Your expression : ").lower().strip()
    if '+' in expression:
        return float(expression.split('+')[0]) + float(expression.split('+')[1])
    elif '-' in expression:
        return float(expression.split('-')[0]) - float(expression.split('-')[1])
    elif '/' in expression:
        return float(expression.split('/')[0]) / float(expression.split('/')[1])
    elif '*' in expression:
        return float(expression.split('*')[0]) * float(expression.split('*')[1])
    else:
        return "Invalid Expression"


# 41
def factorial_sum(num):
    if num > 990:
        return "Please enter numbers under 990 to avoid 'maximum recursion depth exceeded in comparison' error"
    sum_ = 0
    for i in range(1, num+1):
        sum_ += factorial(i)
    return sum_


if __name__ == '__main__':
    pass


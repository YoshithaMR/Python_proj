

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

def print_cubes(n):
    for i in range(1, n+1):
        print(i * i * i)

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def list_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def sort_list(lst):
    return sorted(lst)

def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def max_in_list(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def min_in_list(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

def average_list(lst):
    total = sum_list(lst)
    return total / len(lst)

def count_occurrences(lst, val):
    count = 0
    for item in lst:
        if item == val:
            count += 1
    return count

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def flatten_list(nested_lst):
    flat = []
    for sublist in nested_lst:
        for item in sublist:
            flat.append(item)
    return flat

def merge_lists(lst1, lst2):
    return lst1 + lst2

def repeat_string(s, times):
    return s * times

def greet_multiple(names):
    for name in names:
        greet(name)

def simple_calculator():
    print("Simple Calculator")
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a,b)}")
    print(f"{a} - {b} = {subtract(a,b)}")
    print(f"{a} * {b} = {multiply(a,b)}")
    print(f"{a} / {b} = {divide(a,b)}")

def print_triangle(height):
    for i in range(1, height+1):
        print('*' * i)

def print_inverted_triangle(height):
    for i in range(height, 0, -1):
        print('*' * i)

def print_square(size):
    for _ in range(size):
        print('*' * size)

def print_rectangle(width, height):
    for _ in range(height):
        print('*' * width)

def print_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2*i + 1))
    for i in range(n-2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2*i + 1))

def sum_natural_numbers(n):
    return n * (n + 1) // 2

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def is_perfect_square(n):
    return int(n**0.5)**2 == n

def sum_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == num

def convert_to_binary(num):
    return bin(num)[2:]

def convert_to_hex(num):
    return hex(num)[2:]

def convert_to_octal(num):
    return oct(num)[2:]

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def caesar_cipher(s, shift):
    result = ""
    for char in s:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def count_words(s):
    words = s.split()
    return len(words)

def count_sentences(s):
    return s.count('.') + s.count('!') + s.count('?')

def count_paragraphs(s):
    return s.count('\n\n') + 1

def find_max(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

def find_min(nums):
    min_val = nums[0]
    for n in nums:
        if n < min_val:
            min_val = n
    return min_val

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def linear_search(arr, val):
    for i, item in enumerate(arr):
        if item == val:
            return i
    return -1

def binary_search(arr, val):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid -1
    return -1

def sum_of_squares(n):
    return sum(i*i for i in range(1,n+1))

def sum_of_cubes(n):
    return sum(i*i*i for i in range(1,n+1))

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

def palindrome_number(num):
    return str(num) == str(num)[::-1]

def count_characters(s):
    count = 0
    for _ in s:
        count += 1
    return count

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def print_floyd_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

def print_pascal_triangle(n):
    for i in range(n):
        print(' '*(n-i), end='')
        val = 1
        for j in range(i+1):
            print(val, end=' ')
            val = val * (i - j) // (j + 1)
        print()

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    return a * b // gcd_recursive(a, b)

def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n-1)

def factorial_tail_recursive(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail_recursive(n-1, acc*n)

def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

def power_recursive(base, exp):
    if exp == 0:
        return 1
    return base * power_recursive(base, exp-1)

def flatten_recursive(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_recursive(item))
        else:
            flat.append(item)
    return flat

def count_recursive(lst):
    if not lst:
        return 0
    return 1 + count_recursive(lst[1:])

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def sum_list_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

def max_list_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    max_rest = max_list_recursive(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest

def min_list_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    min_rest = min_list_recursive(lst[1:])
    return lst[0] if lst[0] < min_rest else min_rest

def print_pattern(n):
    for i in range(1, n+1):
        print(''.join(str(j) for j in range(1, i+1)))

def print_reverse_pattern(n):
    for i in range(n, 0, -1):
        print(''.join(str(j) for j in range(1, i+1)))

def print_star_pattern(n):
    for i in range(n):
        print(' '*(n-i-1) + '*'*(2*i+1))

def print_square_pattern(n):
    for _ in range(n):
        print('* '*n)

def sum_even_numbers(n):
    return sum(i for i in range(2, n+1, 2))

def sum_odd_numbers(n):
    return sum(i for i in range(1, n+1, 2))

def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def fibonacci_while(n):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a

def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def binary_to_decimal(b_str):
    return int(b_str, 2)

def decimal_to_binary(num):
    return bin(num)[2:]

def hex_to_decimal(h_str):
    return int(h_str, 16)

def decimal_to_hex(num):
    return hex(num)[2:]

def octal_to_decimal(o_str):
    return int(o_str, 8)

def decimal_to_octal(num):
    return oct(num)[2:]

def temperature_c_to_f(c):
    return (c * 9/5) + 32

def temperature_f_to_c(f):
    return (f - 32) * 5/9

def convert_cm_to_inches(cm):
    return cm / 2.54

def convert_inches_to_cm(inches):
    return inches * 2.54

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def is_vowel(char):
    return char.lower() in 'aeiou'

def is_consonant(char):
    return char.isalpha() and not is_vowel(char)

def greet_formally(name):
    print(f"Good day, {name}. How do you do?")

def greet_informally(name):
    print(f"Hey {name}, what's up?")

def print_alphabet():
    for c in range(ord('a'), ord('z') + 1):
        print(chr(c), end=' ')
    print()

def print_reverse_alphabet():
    for c in range(ord('z'), ord('a') - 1, -1):
        print(chr(c), end=' ')
    print()

def main():
    greet("Alice")
    greet_informally("Bob")
    print(f"5 + 3 = {add(5,3)}")
    print(f"Factorial of 5 is {factorial(5)}")
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(fibonacci(i), end=' ')
    print()
    print("Primes up to 20:", list_primes(20))
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
    print("Sorted list:", sort_list([5,3,6,2,8]))
    print("Unique elements:", unique_elements([1,2,2,3,3,3,4]))
    print("Caesar cipher of 'hello' with shift 3:", caesar_cipher("hello",3))
    print("Is 2024 a leap year?", is_leap_year(2024))
    print("GCD of 48 and 18:", gcd(48, 18))
    print("LCM of 12 and 15:", lcm(12, 15))
    print("Armstrong number check for 153:", is_armstrong(153))
    print("Character frequency in 'hello world':", char_frequency("hello world"))
    print("Palindrome check recursive for 'madam':", is_palindrome_recursive("madam"))
    print("Binary of 42:", convert_to_binary(42))
    print("Decimal of binary 101010:", binary_to_decimal("101010"))
    print("BMI for weight 70kg and height 1.75m:", calculate_bmi(70, 1.75))

if __name__ == "__main__":
    main()


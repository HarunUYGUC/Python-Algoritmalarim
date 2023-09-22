"""
The Fibonacci sequence is defined by the recurrence relation: 
F(n) = F(n-1) + F(n - 2), where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence 
to contain 1000 digits?
"""

a = 1
b = 1
fib_list = [a, b]
last_index = len(fib_list) - 1

while True:
    sum = a + b
    fib_list.append(sum)

    a = b
    b = sum

    last_index += 1

    if (len(str(fib_list[last_index])) == 1000):
        print(last_index + 1)
        break
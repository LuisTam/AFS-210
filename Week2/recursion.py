def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num=1, odd_sum=0):
    # Duplicate the loop1 function using recursion
    if num <= 20:
        if (num % 2) == 1:
            odd_sum += num
        return loop1Rec(num + 1, odd_sum)
    else:
        return odd_sum

def loop2Rec(num=0, even_sum=0):
    # Duplicate the loop2 function using recursion
    if num < 20:
        if (num % 2) == 0:
            even_sum += num
        return loop2Rec(num + 1, even_sum)
    else:
        return even_sum

# Call and print results for each function
print("loop1 result:", loop1())
print("loop1Rec result:", loop1Rec())

print("loop2 result:", loop2())
print("loop2Rec result:", loop2Rec())

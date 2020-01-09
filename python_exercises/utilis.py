def find_largest_num(numbers):
    result = numbers[0]
    for num in numbers:
        if num > result:
            result = num
    return result
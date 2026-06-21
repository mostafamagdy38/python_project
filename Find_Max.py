numbers = [1 , 2, 3, 4, 5, 6]

def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest
        
print(find_max(numbers))
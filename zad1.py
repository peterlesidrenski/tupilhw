numbers = input().split()
repeated_numbers = []
for i in numbers:
    if i not in repeated_numbers:
        print(numbers.count(i))
        repeated_numbers.append(i)
    else:
        continue

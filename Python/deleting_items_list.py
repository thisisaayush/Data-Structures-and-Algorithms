numbers = [2,3,88,202,255,208,6,226,267,288,300,322,355]
numbers.sort()
print(numbers)
start = 0
end = len(numbers)
end_len = 0
min = 200
max = 299

for index, value in enumerate(numbers):
    if value < min:
        start += 1

    elif value > max:
        end_len += 1

end = end - end_len
print(numbers[start:end])
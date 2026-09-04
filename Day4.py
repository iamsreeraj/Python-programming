numbers = [12, 7, 25, 4, 18, 9, 30, 11]

largest = 0
total = 0
i = 0

print("All numbers:")
for x in numbers:
    print(x)

print("\nEven numbers:")
for y in numbers:
    if y % 2 == 0:
        print(y)

for k in numbers:
    total = total + k

print("\nSum of all numbers:")
print(total)

for m in numbers:
    if m > largest:
        largest = m

print("\nLargest number:")
print(largest)

print("\nNumbers until 18:")
while i < len(numbers):
    print(numbers[i])
    if numbers[i] == 18:
        break
    i = i + 1
numbers = []
print("Enter your five numbers\n")

for x in range(5):
    numbers.append(int(input()))
print("The list of numbers are",numbers,"\n")

total = 0
largest = 0
i = 0
lowest = numbers[i]
count =0

for y in numbers:
    total = total + y
print("The total of these numbers:",total)

for z in numbers:
    if z > largest:
        largest = z
print("The largest number is:",largest)

for m in numbers:
    if m < lowest:
        lowest = m
print("The lowest number is:",lowest)

for k in numbers:
    if k % 2==0:
        count = count + 1
print("The count of the even numbers:",count)        




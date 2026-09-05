print("===== STUDENT MARKS SYSTEM =====\n")
name = input("Enter student name:")
print("\n")
maths = int(input("Enter Maths mark:"))
science = int(input("Enter Science mark:"))
english = int(input("Enter English mark:"))
computer =  int(input("Enter Computer mark:"))
history = int(input("Enter History mark:"))
marks = [maths,science,english,computer,history]
print("\n")
print("===== RESULT =====\n")
print("\n")
print("Student:",name)
print("Marks:",marks)
print("\n")
total = 0
highest = 0
i = 0
lowest = marks[i]

average = 0
for x in marks:
    total = total + x
print("Total:",total)

for y in marks:
    if y > highest:
        highest = y
print("Highest:",highest)

for z in marks:
    if z < lowest:
        lowest = z
print("Lowest:",lowest)

count = len(marks)
average = total/count
print("Average:",average)
if total >= 40 and average >62:
 print("Result: PASS")
else:
    print("Result:FAILED") 









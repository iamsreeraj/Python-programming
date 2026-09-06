print("Enter five numbers:")
number = [] #The list to store the numbers from user
 
 #storing numbers into the list
for x in range(5):
    number.append(int(input()))

#The total of the numbers in the list
total = 0
for y in number:
    total = total+y

#The largest number of the list
i = 0
largest = number[i]
for d in number:
    if d > largest:
        largest = d

#smallest number of the list
lowest = number[i]
for z in number:
    if z < lowest:
        lowest = z

#Number of even numbers
count = 0
for m in number:
    if m % 2 ==0:
        count = count+1
        print("Even:",m)

#Number of odd numbers
count1 = 0
for n in number:
    if n % 2 !=0:
        count1 = count1 + 1
        print("Odd:",n)

#Finding the average of the numbers
average = total/len(number)

#Printing the results
print("Numbers:",number)
print("Total:",total)
print("Largest:",largest)
print("Smallest:",lowest)
print("Even numbers:",count)
print("Odd numbers:",count1)
print("\n")
print("Average:",average)
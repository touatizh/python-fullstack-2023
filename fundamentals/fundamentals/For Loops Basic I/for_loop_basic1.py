#Print all integers from 0 to 150
for i in range(151):
    print(i)

print("*"*20)

#Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)

print("*"*20)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

print("*"*20)

#Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)

print("*"*20)

#Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

print("*"*20)

#Flexible Counter
lownum = 4
highnum = 94
mult = 7
for i in range(lownum, highnum+1):
    if i % mult == 0:
        print(i)
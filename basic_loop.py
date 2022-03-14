# Print all integers from 0  to 150
for x in range(0,151):
    print(x)

# Print all the multiples of 5 from to 1,000

for x in range(5,1001,5):
    print(x)

#  Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"

for x in range(1,101):
    if x % 10 == 0 :
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

#  Add odd integers from 0 to 500,000

sum = 0
for x in range(1,500001,2):
    sum += x
print(sum)

#  print postive numbers starting fom 2018

for i in range(2018,0,-4):
    print(i)

#  Flexible Counter:

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum + 1):
    if (i % mult == 0):
        print(i)
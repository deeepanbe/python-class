import sys

n = len(sys.argv)

print('Total Number of Arguments:', n)

print('Name of the Python Script:', sys.argv[0])

print('Arguments Passed:', end = " ")
for i in range(1,n):
    print(sys.argv[i], end= " ")

sum = 0

for i in range(1, n):
    sum += int(sys.argv[i])

print('\nResult:', sum)
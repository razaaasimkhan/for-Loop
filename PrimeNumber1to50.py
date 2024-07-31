def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return number


for number in range(1, 50 + 1): #prime number 1 to 50
    if prime(number):
        print(number)

#2nd method to find the prime number b/w 1 to 50
for n in range(1, 50 + 1):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n)

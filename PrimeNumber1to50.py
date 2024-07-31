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

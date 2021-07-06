import math


def gen_primes():
    num = int(input("Enter a number to specify the range: "))
    num_lst = [i for i in range(2, num + 1)]

    for number in num_lst:
        number = 2
        while number < math.sqrt(num):
            for nr in range(n, num + 1):
                if number * nr in num_lst:
                    num_lst.remove(n * nr)
            number += 1
    print("Prime numbers from the range <2," + str(num) + "> : ", num_lst)


gen_primes()

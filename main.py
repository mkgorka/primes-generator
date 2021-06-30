import math


def gen_primes():
    num = int(input("Enter a number to specify the range: "))
    num_lst = [i for i in range(2, num + 1)]

    for number in num_lst:
        n = 2
        while n < math.sqrt(num):
            for nr in range(n, num + 1):
                if n * nr in num_lst:
                    num_lst.remove(p * nr)
            n += 1
    print("Prime numbers from the range <2," + str(num) + "> : ", num_lst)


gen_primes()

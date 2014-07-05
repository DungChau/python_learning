def main():
    limit = int(input("Please enter the limit range to find primes: "))
    # primes = list(find_primes(limit))
    primes = sieve_of_eratosthenes(limit)
    size = 10
    ps = [primes[i:i+size] for i in range(0, len(primes), size)]
    for p in ps:
        print(p)


def sieve_of_eratosthenes(limit):
    list_of_numbers = [True] * limit

    for i in range(2, int(limit ** (1 / 2)) + 1):
        if list_of_numbers[i]:
            for j in range(i**2, limit, i):
                list_of_numbers[j] = False

    return [x for x in range(2, limit) if list_of_numbers[x]]


def find_primes(limit):
    set_of_primes = set()
    set_of_primes.add(2)

    curr = 2

    while curr < limit:
        curr += 1
        flag = False

        for prime in set_of_primes.copy():
            if curr % prime == 0:
                flag = False
                break
            else:
                flag = True

        if flag:
            set_of_primes.add(curr)

    return set_of_primes


if __name__ == '__main__':
    main()
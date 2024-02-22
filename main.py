prime_store = [2]

print(f"{prime_store[0]} is a prime number...")


def check_if_prime(n):
    li = []
    if n < 2:
        return False
    else:
        for i in range(1, n+1):
            if n % i == 0:
                li.append(i)

    if len(li) == 2:
        return True
    else:
        return False


def gen_prime_number():
    last_prime = prime_store[-1]
    p = last_prime + 1
    # if check_if_prime(p):
    #     prime_store.append(p)
    #     return prime_store[-1]
    # elif not check_if_prime(p):
    #     p += 1
    while not check_if_prime(p):
        p += 1
    prime_store.append(p)

    return f"{prime_store[-1]} is a Prime number..."


def main():

    user_input = ""

    while user_input != "no":
        user_input = input("Next Prime Number? yes or no: ").lower()

        if user_input.isdigit():
            print("Invalid input, input yes or no!")

        elif user_input != "no" and user_input != "yes":
            print("Input should be yes or no!")

        elif user_input == "no":
            print("End...")

        if user_input == "yes":
            r = gen_prime_number()
            print(r)


if __name__ == "__main__":
    main()

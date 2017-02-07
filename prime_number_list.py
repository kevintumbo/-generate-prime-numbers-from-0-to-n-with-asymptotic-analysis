def prime_number_list(n):
    prime_list = []
    # check if n empty
    if n == "":
        return "Input Variable is empty"

    # check if n is integer
    if not isinstance(n, int):
        return "Input Variable should be Integer"

    # check if n is integer
    if n < 0:
        return "Input Variable should be a positive integer"

    # check if n is zero
    if n == 0:
        return "Input Variable cannot be zero"

    # check if n is equal to one
    if n == 1:
        return "Input Variable should be greater than one"

    # list prime numbers
    else:
        for number in range(2, n+1):
            is_prime = True
            for x in range(2, number):
                if number % x == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(number)
    return prime_list
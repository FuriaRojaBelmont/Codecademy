def prime_finder(n):
    primes = []
    for num_to_test in range(2, n + 1):
        is_prime = True 
        for divisor in range(2, num_to_test):
            if num_to_test % divisor == 0:
                is_prime = False
                break  
        if is_prime:
            primes.append(num_to_test)
    return primes

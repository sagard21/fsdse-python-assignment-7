def get_prime_numbers(limit):
    result = []
    for num in range(1, limit):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result.append(num)
    return result
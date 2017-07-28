def get_prime_numbers(num):
	array = []
	for i in range(2, num):
		for x in range(2, i):
			if (i % x) == 0:
				break
		else:
			array.append(i)
	return array

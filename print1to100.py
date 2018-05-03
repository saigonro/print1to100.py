def print_1_to_100(i):
	if i % 3 == 0 and i % 5 == 0:
		return "ThreeFive"
	elif i % 3 == 0:
		return "Three"
	elif i % 5 == 0:
		return "Five"
	else:
		return str(i)

print(" ".join(print_1_to_100(i) for i in range(1, 101)))

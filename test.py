from random import randint

def main():
	M = generate_grid()
	step = randint(0, 15)
	A = (randint(0, len(M[0])), randint(0, len(M)))
	B = (randint(0, len(M[0])), randint(0, len(M)))
	return M, step, A, B

def generate_grid():
	heigh = 15
	width = 15
	half_result = []
	result = []
	for i in range(width):
		for i in range(heigh):
			half_result.append(randint(0, 10000))
		result.append(half_result)
		half_result = []
	return result

if __name__ == "__main__":
	main()
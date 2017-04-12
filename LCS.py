def problem1():
	x = input("Enter the first sequence with no spaces between charecters: ")
	y = input("Enter the second sequence with no spaces between charecters: ")

	#creating the matrix for the top down approach
	matrix = []
	for i in range(len(x)):
		c = []
		for j in range(len(y)):
			c += [None]
		matrix += [c]

	# #setting up the matrix for row0 to be initialized all to 0
	# for col in range(len(y)+1):
	# 	matrix[0][col] = 0

	# #setting up the matrix for col0 to be initialized all to 0
	# for row in range(len(x)+1):
	# 	matrix[row][0] = 0

	#printMatrix(matrix)
	score = LCS(x, y, matrix, len(x), len(y))

	print("The length of a longest common sequence of ")
	print(x)
	print("and")
	print(y)
	print("is " + str(score))
	print()
	print("A longest common subsequence of X and Y is ")
	sequence = problem2(x, y, matrix, len(x), len(y))
	print(sequence)



def problem2(sequenceOne, sequenceTwo, array, i, j):
	#return empty since no charecter to check
	if i==0 or j==0:
		return ""
	#if the two charecters are the same, it is in the sequence
	if sequenceOne[i-1] == sequenceTwo[j-1]:
		return problem2(sequenceOne, sequenceTwo, array, i-1, j-1) + \
			sequenceOne[i-1]
	else:
		#if not the same, choose the higher score of the two to traverse towards
		topScore = array[i-2][j-1]
		leftScore = array[i-1][j-2]

		if topScore!= None and leftScore != None and topScore >= leftScore:
			return problem2(sequenceOne, sequenceTwo, array, i-1, j)
		else:
			return problem2(sequenceOne, sequenceTwo, array, i, j-1)

def LCS(sequenceOne, sequenceTwo, array, i, j):
	#return 0 since no charecter to check
	if i==0 or j==0:
		return 0

	#check if value is already in memoized
	elif array[i-1][j-1] != None:
		return array[i-1][j-1]

	#last two letters match
	if sequenceOne[i-1] == sequenceTwo[j-1]:
		#check if the value is in the previous
		if array[i-1][j-1] != None:
			return 1 + array[i-1][j-1]
		else:
			#value is not in the previous so call lcs with both letters chopped off
			score = LCS(sequenceOne, sequenceTwo, array, i-1, j-1) + 1
			#memoize result and return the score
			array[i-1][j-1] = score
			return score



	else:
		#throw out both charecters but check the case for each and take the max score
		score = max(LCS(sequenceOne, sequenceTwo, array, i-1, j), \
			LCS(sequenceOne, sequenceTwo, array, i, j-1))
		#memoize result and return the score
		array[i-1][j-1] = score
		return score



def printMatrix(array):
	for i in range(len(array)):
		for j in range(len(array[0])):
			print(array[i][j] , end = " ")
		print()

problem1()
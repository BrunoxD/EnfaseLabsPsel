"""
	For the development of this function I assumed
	that there will be repeated entries, 
	like the real sequence of fibonacci 0, 1, 1, 2, 3.
"""
def fibonacian(n, A):
	max_sequence = 0	

	for i in range(0, n):		
		for j in range(i+1, n):
			fibo = A.copy()

			# Ensures first element <= second element.
			a = min(A[i], A[j])
			b = max(A[i], A[j])

			# There is no sequence between to negative elements.
			if(a < 0 and b < 0):
				continue

			# Compose the sequence and removes from the list.
			counter = 2
			sequence = [a, b]
			fibo.remove(a)
			fibo.remove(b)

			# Checks the sequence for the next element.
			while(a+b in fibo):
				c = a
				a = b
				b = a + c
				counter += 1
				sequence.append(b)
				fibo.remove(b)

			# Check for the longest sequence.
			if(counter >= max_sequence):
				max_sequence = counter
				final_sequence = sequence

	return final_sequence, max_sequence

if __name__ == '__main__':
	# Reading the inputs n and sequence.
	n = int(input())
	sequence = list(map(int, input().split()))

	# Remove [1] to see the sequence found.
	print(fibonacian(n, sequence)[1])

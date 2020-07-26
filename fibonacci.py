from functools import lru_cache
from time import perf_counter

# Fibonacci sequence starting with 1,1
# In this case for every recursion all numbers are re-calculated
def fib(n):
	return 1 if n <= 1 else fib(n-1) + fib(n-2)

# Fibonacci sequence with memoization using dict
# In this case for every recursion we check if the result is present
# on the global dict fib_cache, if it is we return the value if not we add it
fib_cache = {}
def fib_dict(n):
	if n <= 1:
		return 1
	if n not in fib_cache:
		fib_cache[n-1] = fib_dict(n-1) + fib_dict(n-2)
	return fib_cache[n-1]

# Fibonacci sequence with memoization using Least Recently Used property
# In this case we use the lru_cache property to automaticaly cache the function results
# it has the same behaviour as above but we don't need to use a global dict
@lru_cache(maxsize = 2000)
def fib_lru(n):
	return 1 if n <= 1 else fib_lru(n-1) + fib_lru(n-2)

# Timing the functions for a number
def fibonacci_times(n):
	# Array with all fibonacci functions to iterate through
	fibs = [fib,fib_dict,fib_lru]
	# Using perf_counter to get the time in seconds
	for fibonacci in fibs:
		t_start = perf_counter()
		temp_f = fibonacci(n)
		t_end = perf_counter()
		print(f"Function {fibonacci.__name__} for {n+1} with result {temp_f} took {t_end - t_start:0.4f} in seconds")


def main():
	# Defining a input loop that forces the user to input an integer
	n = ''
	while not isinstance(n,int):
		n = input('Insert a number to check Fibonacci times: ')
		try:
			n = int(n)
		except:
			print('Invalid input')
	print(f"\nFibonacci array: {[fib_lru(n) for n in range(n)]}\n")
	fibonacci_times(n-1)

if __name__ == '__main__':
	main()
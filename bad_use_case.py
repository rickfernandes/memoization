from functools import lru_cache
from random import randint

# Explanation: If you have a funciton that has a dynamic return value (it updates with every call)
# you should not use lru_cache

# This is an example where NOT to use the lru_cache
@lru_cache(maxsize=10)
def random_n_lru(n):
	# This function should always return a random number
	# by using the lru_cache we're making a static connection between
	# n and the first result of the function for that number
	return randint(n,n*100) 

def random_number(n):
	# Without lru_cache the numbers will always be random
	return randint(n,n*100) 

def main():
	n = ''
	while not isinstance(n,int):
		n = input('Insert a number: ')
		try:
			n = int(n)
		except:
			print('Invalid input')
	for i in range(1,6):
		# This for shows how static is random_n_lru. Notice that we have a maxsize=10 for lru_cache, so
		# if you pass a n > 10 you will start getting random values because the new ones will replace the old ones
		print(f"{i} interation of function random_number with lru_cache:{[random_n_lru(n) for n in range(1,n+1)]}")
	for i in range(1,6):
		# This for shows the correct expected random behaviour
		print(f"{i} interation of function random_number without lru_cache:{[random_number(n) for n in range(1,n+1)]}")

if __name__ == '__main__':
	main()
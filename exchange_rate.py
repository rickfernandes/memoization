from functools import lru_cache
from time import perf_counter
from requests import get
from json import loads
import datetime as dt


# Example where a costly function can be improved by using lru_cache



@lru_cache(maxsize=365)
# Maxsize here is 365 to store up to one year of exchange rates
def date_exchange_rates_lru(date):
	# Function to query the exchange daily exchange rate via API using lru_cache
	response = get(url = f"https://api.exchangeratesapi.io/{date}?base=EUR")
	# Using the json module to convert the JSON response from the API into a dict
	return loads(response.content)['rates']

def rate_lru(date,currency):
	# Function to get the exchange rate for a currency in a specific date
	# uses the function with lru_cache
	return date_exchange_rates_lru(date)[currency]

def date_exchange_rates(date):
	# Function to query the exchange daily exchange rate via API without using lru_cache
	response = get(url = f"https://api.exchangeratesapi.io/{date}?base=EUR")
	return loads(response.content)['rates']

def rate(date,currency):
	# Function to get the exchange rate for a currency in a specific date
	# uses the function without lru_cache
	return date_exchange_rates(date)[currency]

def get_balance():
	# This function creates a generic balance statement
	balance = {}
	# Using the datetime module to work with dates/periods
	initial_day = dt.date(2020,6,1)
	final_day = dt.date(2020,6,30)
	delta = abs(final_day - initial_day).days
	balance_value = 100
	for i in range(delta+1):
		day = (initial_day + dt.timedelta(days=i))
		if day.month //2 == day.month / 2:
			balance_value += 5
			balance.update({day.isoformat():balance_value})
		else:
			balance_value -= 4
			balance.update({day.isoformat():balance_value})
	return balance


def main():
	# Creates the balance dict with days as keys
	balance = get_balance()

	# Prints the results of the exchange rates (with lru_cache)
	print("Applying exchange rate with lru_cache")
	t_start = perf_counter()
	for m in balance:
		print(f"{m}: EUR={balance[m]:0.2f} | CAD={balance[m]*rate_lru(m,'CAD'):0.2f} | USD={balance[m]*rate_lru(m,'USD'):0.2f} | GBP={balance[m]*rate_lru(m,'GBP'):0.2f}")
	t_end = perf_counter()
	t_lru = t_end - t_start
	print("---------------------------")
	# Prints the results of the exchange rates (without lru_cache)
	print("Applying exchange rate without lru_cache")
	t_start = perf_counter()
	for m in balance:
		print(f"{m}: EUR={balance[m]:0.2f} | CAD={balance[m]*rate(m,'CAD'):0.2f} | USD={balance[m]*rate(m,'USD'):0.2f} | GBP={balance[m]*rate(m,'GBP'):0.2f}")
	t_end = perf_counter()
	t = t_end - t_start

	print("---------------------------")
	print(f"With lru_cache it took {t_lru:0.4f} while without took {t:0.4f} seconds")



if __name__ == '__main__':
	main()
# Memoization in Python #

_*This repository shows how to apply memoization in Python.*_

### Definition ###
According to [Wikipedia](https://en.wikipedia.org/wiki/Memoization):
> In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

---

## Repository explanation ##
This repository has 3 code examples that use memoization. I advise to check them in the order below:

### Fibonacci ###
This code shows the time difference between 3 approaches for a recursive function:
1. Without memoization
2. With memoization using a dict
3. With memoization using a well establish Python module

### Bad Use Case ###
This code shows how an improper use of memoization might generate an undesired behaviour.
The main takeaway here is that you should **never** use memoization if a function potentially has different results for the same input.

### Exchange Rate ###
This code shows how memoization improves execution time when using a costly function (like a GET request). Another side advantage here is that if the API server is down
or times out, you will still have the [lru_cache](https://www.geeksforgeeks.org/python-functools-lru_cache/) from previous calls.

---

### Notes: ###
*All codes use Python3*
Modules used:

|Module|Attribute|
|:-----|:-----|
|functools|lru_cache|
|random|randint|
|time|perf_counter|
|requests|get|
|json|loads|
|datetime|*several*|
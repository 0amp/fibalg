import numpy as np
import time

def fib_recursive(n): 
  if n == 0: 
    return 0
  elif n == 1: 
    return 1
  else: 
    return fib_recursive(n-1) + fib_recursive(n-2)
  
def fib_iterative(n): 
  n_0 = 0 
  n_1 = 1
  if n == 0: 
    return 0
  for i in range(1,n): 
    n_1 = n_0 + n_1
    n_0 = n_1 - n_0
  return n_1

def expon_matrix(m, n): 
  # implementing O(log(n)) matrix exponentiation algorithm
  if n == 1: 
    return m
  if n%2 == 0: 
    temp = expon_matrix(m, n/2)
    return np.matmul(temp, temp)
  else: 
    return np.matmul(expon_matrix(m, n-1), m)

def fib_matrix(n): 
  fib_matrix = np.array([[0, 1], [1, 1]], dtype=object)
  fib_start = np.array([[0], [1]], dtype=object)
  return np.matmul(expon_matrix(fib_matrix, n), fib_start)

num = 15

start_time = time.time()
print(fib_matrix(num)[0][0])
print(time.time() - start_time)

start_time = time.time()
print(fib_iterative(num))
print(time.time() - start_time)

start_time = time.time()
print(fib_recursive(num))
print(time.time() - start_time)


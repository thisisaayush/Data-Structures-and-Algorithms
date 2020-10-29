def sum_divisors(n):
  sum = 0
  num = 1;
  # Return the sum of all divisors of n, not including n

  while num < n:
    if(n % num == 0):
      sum += num
      num += 1
  return sum

print(sum_divisors(0))
print(sum_divisors(4)) 
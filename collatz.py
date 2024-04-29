def collatz(value):
  if value % 2 == 0:
    print(value // 2)

    return value // 2
  elif value % 2 == 1:
    result = 3 * value + 1

    print(result)

    return result
  
try:
  n = input("Type a number: ")
  
  while n != 1:
    n = collatz(int(n))
except ValueError:
  print('You must enter an integer type.')

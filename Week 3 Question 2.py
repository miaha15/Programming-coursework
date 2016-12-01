'http://www.counton.org/explorer/primes/checking-if-a-number-is-prime/'
'http://stackoverflow.com/questions/14656473/python-beginners-loop-finding-primes'

'''
PSUEDO CODE

A <= users input

 PRIMECHECKER[X, Y=2]
    IF [X] = 1 THEN
      RETURN FALSE
   IF [X] = 2 THEN
      RETURN TRUE
    IF [X] % [Y] = 0 THEN
      RETURN FALSE
    IF [Y] >= [X]/[Y] + 1 THEN
      RETURN TRUE
    IF [X] = 3 THEN
      RETURN TRUE
    RETURN PRIMECHECKER[X,Y+1]

PRIMECHECKER[A]

'''

CheckPrime = int(input("Enter number here: "))

def primeChecker(number, divisor = 2):
   if number == 1:
      return False
   if number == 2:
      return True
   if number % divisor == 0:
      return False
   if divisor >= number/2 + 1:
      return True
   if number == 3:
      return True
   return primeChecker(number,divisor + 1)

print(primeChecker(CheckPrime))


# Check if n is prime
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    
    return True

# Added this later to demonstrate how this appraoch can be extended easily
# with arbitary computations. Creates a tag for prime numbers
def primeTag(tag):
    return lambda n, acc: acc + tag if isPrime(n) else acc

# Basic FizzBuzz Implementation. Creates a tag for multiples of the divisor
def modTag(divisor, tag):
    return lambda dividend, acc: acc + tag if dividend % divisor == 0 else acc

# Default number for FizzBuzz
def defaultNum(n, acc):
    return acc if len(acc) > 0 else str(n)

# This is effectively a Kleisli Composition of the passed in functions 
# (Applied to the whole list like Haskell's foldl')
def composeAndRun(*fns):
    def bound(a):
        acc = ""
        for fn in fns:
            acc = fn(a, acc)
        return acc
    return bound

# Almost-Monads ftw, you can pretty easily see how to extend this with arbitrary computations
# I just created a new function called primeTag that has completely different rules for 
# what it does to the printed output and it composes all the same here
fizzbuzz = composeAndRun(
    modTag(3, "Fizz"),
    primeTag("Prime"),
    modTag(5, "Buzz"),
    defaultNum
)

# Apply the computations and run the given effect
def travel(nums, comp, effect):
    for s in map(comp, nums):
        effect(s)

# Running the program. 
travel(range(1,21,1), fizzbuzz, print)
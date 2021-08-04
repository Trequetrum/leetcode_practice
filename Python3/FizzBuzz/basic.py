def fizzbuzz(n):
    if n % (3 * 5) == 0: return "FizzBuzz"
    if n % 3 == 0: return "Fizz"
    if n % 5 == 0: return "Buzz"
    return str(n)

def travel(nums, comp, effect):
    for n in nums:
        effect(comp(n))

travel(range(1,21,1), fizzbuzz, print)
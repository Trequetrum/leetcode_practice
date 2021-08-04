def modTag(divisor, tag):
    return lambda dividend, acc: acc + tag if dividend % divisor == 0 else acc

def defaultNum(n, acc):
    return acc if len(acc) > 0 else str(n)

def composeAndRun(*fns):
    def bound(a):
        acc = ""
        for fn in fns:
            acc = fn(a, acc)
        return acc
    return bound

fizzbuzz = composeAndRun(
    modTag(3, "Fizz"), 
    modTag(5, "Buzz"), 
    defaultNum
)

def travel(nums, comp, effect):
    for s in map(comp, nums):
        effect(s)

travel(range(1,21,1), fizzbuzz, print)
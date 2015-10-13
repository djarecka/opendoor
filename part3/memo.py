from collections import OrderedDict


def memoize(f, k):
    memo = OrderedDict()
    def helper(x):
        if x not in memo:
            if len(memo) == k:
                print "pop item from memo", memo.popitem(last=False)
            memo[x] = f(x)
            print "NOT in memo", x
        else:
            print "in memo", x
        return memo[x]
    return helper


# example of usage for a simple function
def fun(n):
    return n**2

fun = memoize(fun, 2)

print fun(4)
print fun(6)
print fun(4)
print fun(5)
print fun(4)

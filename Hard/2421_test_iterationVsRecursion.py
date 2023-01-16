
import functools
import timeit
N = 998
import sys
# print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)


parent = list(range(N))



def test_recursion(i=N-1):
    # print(i, parent[i])
    if i != parent[i]:
        parent[i] = test_recursion(parent[i])
    return parent[i]

def test_iteration(i=N-1):
    while i != parent[i]:
        # print(i, parent[i])
        i = parent[i]
    return i

def main():
    sys.setrecursionlimit(2000)
    @functools.cache
    def fib(n=N):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    # for i in range(N):
    #     parent[i] = i - 1
    # parent[0] = 0
    # print(f"{timeit.timeit(test_recursion, number=1):5f}")

    # for i in range(N):
    #     parent[i] = i - 1
    # parent[0] = 0
    # # print(parent)
    # print(f"{timeit.timeit(test_iteration, number=1):5f}")
    
    print(f"{timeit.timeit(fib, number=1):5f}")


main()
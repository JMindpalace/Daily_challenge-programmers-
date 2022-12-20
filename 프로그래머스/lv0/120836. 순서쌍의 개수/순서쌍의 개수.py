def solution(n):
    return len([ i for i in range(1, n+1) if n%i == 0 ])

# len(list(filter(lambda v: n % (v+1) == 0, range(n))))

def solution(n, t):
    a = (n*2) 
    for i in range(1, t):
        a *= 2
        
    return a

# 2**t * n  # n*(2**t)
# n << t

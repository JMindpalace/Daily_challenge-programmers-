import math
def solution(n):
    return 1 if math.sqrt(n) == int(math.sqrt(n)) else 2

# 1 if (n ** 0.5).is_integer() else 2

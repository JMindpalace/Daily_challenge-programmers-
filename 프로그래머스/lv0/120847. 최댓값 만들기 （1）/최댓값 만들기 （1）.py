def solution(n):
    answer = n.pop(n.index(max(n))) * n.pop(n.index(max(n)))
    return answer

# n.sort()
# n[-2] * n[-1]
def solution(my_str, n):
    return [my_str[x-n:x] for x in range(n, len(my_str)+n, n)]
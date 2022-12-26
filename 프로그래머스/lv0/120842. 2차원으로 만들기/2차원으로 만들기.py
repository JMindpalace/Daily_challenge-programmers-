def solution(num_list, n):
    a, b = [], []
    for i, num in enumerate(num_list):
        b.append(num)
        if (i+1) % n == 0:
            a.append(b)
            b = []
    return a
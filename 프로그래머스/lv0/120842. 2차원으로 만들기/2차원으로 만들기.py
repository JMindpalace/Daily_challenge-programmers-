def solution(num_list, n):
    a, b = [], []
    for i, num in enumerate(num_list):
        b.append(num)
        if (i+1) % n == 0:
            a.append(b)
            b = []
    return a

# [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]

# li = np.array(num_list).reshape(-1,n)
# return li.tolist()

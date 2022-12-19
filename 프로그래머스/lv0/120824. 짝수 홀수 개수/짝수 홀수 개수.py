def solution(num_list):
    a = len([ i for i in num_list if i%2 == 1 ])
    return [ len(num_list)-a, a]

# # 
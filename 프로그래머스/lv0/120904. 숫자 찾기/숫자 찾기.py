def solution(num, k):
    for i in str(num):
        if int(i)==k:
            answer = str(num).index(i)+1
            break
        else:
            answer = -1
    return answer

# -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

"""
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1
"""

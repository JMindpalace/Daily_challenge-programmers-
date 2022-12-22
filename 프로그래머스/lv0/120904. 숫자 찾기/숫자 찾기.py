def solution(num, k):
    for i in str(num):
        if int(i)==k:
            answer = str(num).index(i)+1
            break
        else:
            answer = -1
    return answer
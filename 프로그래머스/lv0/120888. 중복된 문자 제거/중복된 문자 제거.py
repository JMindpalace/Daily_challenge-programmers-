def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i not in answer:
            answer += i
    
    return answer

# ''.join(dict.fromkeys(my_string))
# 딕셔너리 형식으로의 변환으로 list의 중복 제거

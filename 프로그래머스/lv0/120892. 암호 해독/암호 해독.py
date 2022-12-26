def solution(cipher, code):
    return ''.join([ v for i, v in enumerate(cipher) if (i+1)%code==0 ])

# cipher[code-1::code]
# 문자열 [시작:끝:점프]

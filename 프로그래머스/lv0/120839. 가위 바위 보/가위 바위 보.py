def solution(rsp):
    return ''.join([ str(0) if int(i)==2 else ( str(5) if int(i)==0 else str(2)) for i in rsp ])

# 딕셔너리 방법 추가
# d = {'0':'5','2':'0','5':'2'}
# return ''.join(d[i] for i in rsp)

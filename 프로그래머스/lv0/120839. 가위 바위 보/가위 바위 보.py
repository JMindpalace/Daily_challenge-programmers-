def solution(rsp):
    return ''.join([ str(0) if int(i)==2 else ( str(5) if int(i)==0 else str(2)) for i in rsp ])
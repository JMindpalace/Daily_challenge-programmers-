def solution(array):
    return sum([ 1 for i in str(array) if ((i.isdigit()) and (int(i)%7==0) and (int(i)>0) ) ])

# str(array).count('7')

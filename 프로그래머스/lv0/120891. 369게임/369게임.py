def solution(order):
    return sum([ 1 for i in str(order) if ( (int(i)%3==0) and (int(i)>0)) ])

# sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
# order.count('3') + order.count('6') + order.count('9')

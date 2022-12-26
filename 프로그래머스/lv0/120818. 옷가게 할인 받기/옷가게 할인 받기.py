def solution(price):
    if price < 100000:
        return price
    elif price < 300000:
        return int(price * 0.95)
    elif price < 500000:
        return int(price * 0.9)
    else:
        return int(price * 0.8)
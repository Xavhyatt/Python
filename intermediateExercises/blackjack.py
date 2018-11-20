def blackjack(a,b):
    if a>=b and a<=21 and a>0:
        return a

    if b>21 and a<=21 and a>0:
        return a

    if b>a and b<=21 and b>0:
        return b

    if a>21 and b<=21 and b>0:
        return b

    else:
        return 0


print(blackjack(-1,-1))